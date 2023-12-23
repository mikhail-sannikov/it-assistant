from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .models import Object, Theme, EducationalResource
from .forms import AddSummary


class MainLearningPage(ListView):
    model = Object
    template_name = 'learning/main_learning_page.html'


class ThemesList(ListView):
    model = Theme
    template_name = 'learning/object_themes.html'

    def get_queryset(self):
        return (Object.objects.get(name=self.kwargs['learning_str'])
                .theme_data.all())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.kwargs['learning_str']
        return context


class ThemeView(FormView):
    template_name = 'learning/theme.html'
    form_class = AddSummary

    def form_valid(self, form):
        theme = Theme.objects.get(theme=self.kwargs['theme_str'])
        element = Object.objects.get(name=self.kwargs['learning_str'])

        if not element.is_active:
            element.is_active = True

        if theme.summary is not None:
            theme.summary += self.request.POST.get('summary')
            theme.save()

        if self.request.POST.get('passed_theme') == 'true':
            theme.passed_theme = True
            theme.save()
            element.progress = (Theme.objects.filter(passed_theme=True).count()
                                / Theme.objects.count() * 100)
        elif self.request.POST.get('passed_theme') == 'false':
            theme.passed_theme = False
            theme.save()
            element.progress = (Theme.objects.filter(passed_theme=True).count()
                                / Theme.objects.count() * 100)
            if element.progress == 0:
                element.is_active = False

        element.save()

        return redirect(reverse_lazy('theme',
                                     args=[self.kwargs['learning_str'],
                                           self.kwargs['theme_str']]))

    def get_context_data(self, **kwargs):
        theme = Theme.objects.get(theme=self.kwargs['theme_str'])

        context = super().get_context_data(**kwargs)
        context['summary'] = theme.summary
        context['resources'] = theme.educational_data.all()
        context['resources_count'] = theme.educational_data.count()

        return context
