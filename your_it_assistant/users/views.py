from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View, generic

from users.forms import UserCreationForm

from user_tests.models import Test, TestsList
from learning.models import UserObjectData, UserThemeData, Object, Theme
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

            for test in Test.objects.all():  # создаем тесты в БД
                element = TestsList(test=test,
                                    user=User.objects
                                    .get(username=username))
                element.save()

            for obj in Object.objects.all():
                element = UserObjectData(is_active=0,
                                         object=obj,
                                         user=User.objects
                                         .get(username=username))
                element.save()

            for item in UserThemeData.objects.all():
                element = UserThemeData(object=item.object,
                                        theme=item.theme,
                                        user=User.objects.
                                        get(username=username))
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_active'] = (UserObjectData.objects
                                .filter(user=self.request.user,
                                        is_active=True)
                                .count())

        context['active_data'] = (UserObjectData.objects
                                  .filter(user=self.request.user))

        return context
