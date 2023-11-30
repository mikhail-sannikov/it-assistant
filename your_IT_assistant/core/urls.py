from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('info/', views.InfoPage.as_view(), name='info')
]
