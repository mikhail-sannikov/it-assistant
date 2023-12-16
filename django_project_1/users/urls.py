from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.Register.as_view(), name='register'),
    path('tests/', views.TestsList.as_view(), name='tests'),
    path('tests/<str:test_str>/',
         views.TestPreview.as_view(),
         name='test_preview'),
    path('question/<int:question_id>/',
         views.Test.as_view(),
         name='question'),
    path('profile/', views.Profile.as_view(), name='profile')
]
