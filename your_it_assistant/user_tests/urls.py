from django.urls import path

from .views import TestView, TestsListView, TestPreviewView

urlpatterns = [
    path('tests/', TestsListView.as_view(), name='tests'),
    path('tests/<str:test_str>/',
         TestPreviewView.as_view(),
         name='test_preview'),
    path('question/<int:question_id>/',
         TestView.as_view(),
         name='question'),
]
