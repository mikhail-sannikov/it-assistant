from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View, generic

from users.forms import UserCreationForm

from user_tests.models import Test, TestsList
from .models import User


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

            for test in Test.objects.all():
                element = TestsList(test=test, user=User
                                    .objects
                                    .get(username=username))
                element.save()

            return redirect('home')

        context = {
            'form': form
        }
        return render(request=request,
                      template_name=self.template_name,
                      context=context)


class Profile(generic.ListView):
    template_name = 'users/profile.html'

    def get_queryset(self):
        queryset = TestsList.objects.filter(user=self.request.user)
        return queryset
