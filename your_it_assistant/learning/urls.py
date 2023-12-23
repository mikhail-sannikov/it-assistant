from django.urls import path, include

from .views import MainLearningPage, ThemesView, Resources

urlpatterns = [
    path('learning/', MainLearningPage.as_view(), name='learning'),
    path('learning/<str:learning_str>/', ThemesView.as_view(), name='object'),
    path('learning/<str:learning_str>/resources/',
         Resources.as_view(),
         name='resources'),
]
