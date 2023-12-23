from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from .models import Object, ThemeList, EducationalResource
from .forms import AddSummary


class MainLearningPage(ListView):
    model = Object
    template_name = 'learning/main_learning_page.html'


class ThemesView(ListView):
    model = ThemeList
    template_name = 'learning/object_themes.html'

    def get_queryset(self):
        return (Object.objects.get(name=self.kwargs['learning_str'])
                .theme_data.all())


class Resources(FormView):
    template_name = 'learning/resources.html'
    form_class = AddSummary
    success_url = reverse_lazy()

    def form_valid(self, form):
        form.save()
        return redirect(self.get_success_url())
