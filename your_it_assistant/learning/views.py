from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .models import Object, Theme, UserThemeData, UserObjectData
from .forms import AddSummary


class MainLearningPage(ListView):
    model = Object
    template_name = 'learning/main_learning_page.html'


class ThemesList(ListView):
    model = UserThemeData
    template_name = 'learning/object_themes.html'

    def get_queryset(self):
        object = Object.objects.get(object=self.kwargs['learning_str'])
        return self.model.objects.filter(user=self.request.user,
                                         object=object)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.kwargs['learning_str']

        return context


class ThemeView(FormView):
    template_name = 'learning/theme.html'
    form_class = AddSummary

    def form_valid(self, form):
        need_theme = Theme.objects.get(theme=self.kwargs['theme_str'])
        need_object = Object.objects.get(object=self.kwargs['learning_str'])

        theme = (UserThemeData.objects
                 .get(user=self.request.user,
                      object=need_object,
                      theme=need_theme))

        element = (UserObjectData.objects
                   .get(user=self.request.user,
                        object=need_object))

        if not element.is_active:
            element.is_active = True

        if self.request.POST.get('summary') != '':
            if theme.summary is None:
                theme.summary = self.request.POST.get('summary')
            else:
                theme.summary += self.request.POST.get('summary')
            theme.save()

        if self.request.POST.get('passed_theme') == 'true':
            theme.passed_theme = True
            theme.save()
            element.progress = (UserThemeData.objects
                                .filter(user=self.request.user,
                                        object=need_object,
                                        passed_theme=True)
                                .count()
                                / UserThemeData.objects
                                .filter(user=self.request.user,
                                        object=need_object).count() * 100)
        elif self.request.POST.get('passed_theme') == 'false':
            theme.passed_theme = False
            theme.save()
            element.progress = (UserThemeData.objects
                                .filter(user=self.request.user,
                                        object=need_object,
                                        passed_theme=True)
                                .count()
                                / UserThemeData.objects
                                .filter(user=self.request.user,
                                        object=need_object).count() * 100)
        if element.progress == 0:
            element.is_active = False

        element.save()

        return redirect(reverse_lazy('theme',
                                     args=[self.kwargs['learning_str'],
                                           self.kwargs['theme_str']]))

    def get_context_data(self, **kwargs):
        theme = Theme.objects.get(theme=self.kwargs['theme_str'])
        need_object = Object.objects.get(object=self.kwargs['learning_str'])

        context = super().get_context_data(**kwargs)
        context['summary'] = ((UserThemeData.objects
                              .get(user=self.request.user,
                                   object=need_object,
                                   theme=theme))
                              .summary)
        context['resources'] = theme.educational_data.all()
        context['resources_count'] = theme.educational_data.count()

        return context
