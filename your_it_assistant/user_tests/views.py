from django.shortcuts import render, redirect
from django.views import View

from .models import Test, TestsList, Answer


class TestsListView(View):
    test_data = Test.objects.all()

    template_name = 'user_tests/tests.html/'
    context = {
        'test_data': test_data
    }

    def get(self, request):
        return render(request=request,
                      template_name=self.template_name,
                      context=self.context)


class TestPreviewView(View):
    template_name = 'user_tests/tests_preview.html/'

    def get(self, request, test_str):
        if Answer.objects.count() > 0:
            Answer.objects.all().delete()

        context = {
            'test_str': test_str,
        }
        return render(request=request,
                      template_name=self.template_name,
                      context=context)


class TestView(View):
    template_name = 'user_tests/test.html/'

    def get(self, request, question_id):
        got_title = request.GET['title']
        test_data = Test.objects.get(title=got_title)

        if question_id + 1 > test_data.question.count():
            context = {
                'grade': (Answer.objects.filter(right=1).count()
                          / test_data.question.count() * 100),
                'wrongs': Answer.objects.filter(right=0),
                'wrongs_counter': Answer.objects.filter(right=0).count(),
                'got_title': got_title
            }

            return render(request=request,
                          template_name='user_tests/test_result.html',
                          context=context)

        questions = test_data.question.all()
        question = questions[question_id]

        context = {
            'got_title': got_title,
            'question': question,
            'question_id': question_id+1,
            'test_data': test_data,
        }

        return render(request=request,
                      template_name=self.template_name,
                      context=context)

    def post(self, request, question_id):
        got_title = request.POST['title']
        test_data = Test.objects.get(title=got_title)

        if question_id + 1 > test_data.question.count():
            expression = (Answer.objects.filter(right=1).count()
                          / test_data.question.count() * 100)

            (TestsList.objects
             .filter(user=request.user, test=test_data)
             .update(grade=expression))
            Answer.objects.all().delete()

            return redirect('home')

        questions = test_data.question.all()
        question = questions[question_id]

        context = {
            'got_title': got_title,
            'question': question,
            'question_id': question_id + 1,
            'test_data': test_data,
        }

        if request.POST['answer'] != question.answer:
            if Answer.objects.count() != question_id:
                Answer.objects.last().delete()

            element = Answer(answer=question,
                             explanation=question.explanation,
                             right=0)
            element.save()
        else:
            if Answer.objects.count() != question_id:
                Answer.objects.last().delete()

            element = Answer(right=1)
            element.save()

        return render(request=request,
                      template_name=self.template_name,
                      context=context)
