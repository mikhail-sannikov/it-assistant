from django.urls import path, include

from .views import MainLearningPage, ThemesList, ThemeView

urlpatterns = [
    path('learning/', MainLearningPage.as_view(), name='learning'),
    path('learning/<str:learning_str>/', ThemesList.as_view(), name='object'),
    path('learning/<str:learning_str>/<str:theme_str>/',
         ThemeView.as_view(),
         name='theme'),
]
