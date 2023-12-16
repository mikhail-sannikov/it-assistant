from django.shortcuts import render, redirect
from django.views import View

from .models import Test, TestsList, WrongAnswer


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
                'grade': ((test_data.question.count()
                           - WrongAnswer.objects.count())
                          / test_data.question.count() * 100),
                'wrongs': WrongAnswer.objects.all(),
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

        if (question_id + 1 > test_data.question.count()
                and request.POST['finish'] == '1'):

            expression = ((test_data.question.count()
                           - WrongAnswer.objects.count())
                          / test_data.question.count() * 100)

            TestsList.objects.filter(user=request.user,
                                            test=test_data).update(
                grade=expression)
            WrongAnswer.objects.all().delete()
            return redirect('home')

        questions = test_data.question.all()
        question = questions[question_id]

        context = {
            'got_title': got_title,
            'question': question,
            'question_id': question_id + 1,
            'test_data': test_data,
        }

        if request.POST['btn'] != question.answer:
            element = WrongAnswer(wrong_answer=question,
                                  explanation=question.explanation)
            element.save()

        return render(request=request,
                      template_name=self.template_name,
                      context=context)
