from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View, generic

from users.forms import UserCreationForm
from . import models


class Register(View):
    template_name = 'registration/registration.html/'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request=request,
                      template_name=self.template_name,
                      context=context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

        context = {
            'form': form
        }
        return render(request=request,
                      template_name=self.template_name,
                      context=context)


class TestsList(View):
    test_data = models.Test.objects.all()

    template_name = 'users/tests.html/'
    context = {
        'test_data': test_data
    }

    def get(self, request):
        return render(request=request,
                      template_name=self.template_name,
                      context=self.context)


class TestPreview(View):
    template_name = 'users/tests_preview.html/'

    def get(self, request, test_str):
        context = {
            'test_str': test_str,
        }
        return render(request=request,
                      template_name=self.template_name,
                      context=context)


class Test(View):
    template_name = 'users/test.html/'

    def get(self, request, question_id):
        got_title = request.GET['title']
        test_data = models.Test.objects.get(title=got_title)

        if question_id + 1 > test_data.question.count():
            context = {
                'grade': ((test_data.question.count()
                           - models.WrongAnswer.objects.count())
                          / test_data.question.count() * 100),
                'wrongs': models.WrongAnswer.objects.all(),
                'got_title': got_title
            }

            return render(request=request,
                          template_name='users/test_result.html',
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
        test_data = models.Test.objects.get(title=got_title)

        if (question_id + 1 > test_data.question.count()
                and request.POST['finish'] == '1'):
            expression = ((test_data.question.count()
                           - models.WrongAnswer.objects.count())
                          / test_data.question.count() * 100)
            models.TestsList.objects.filter(user=request.user, test=test_data).update(grade=expression)
            models.WrongAnswer.objects.all().delete()
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
            element = models.WrongAnswer(wrong_answer=question,
                                         explanation=question.explanation)
            element.save()

        return render(request=request,
                      template_name=self.template_name,
                      context=context)


class Profile(generic.ListView):
    template_name = 'users/profile.html'

    def get_queryset(self):
        queryset = models.TestsList.objects.filter(user=self.request.user)
        return queryset
