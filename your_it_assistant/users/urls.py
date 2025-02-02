from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.Register.as_view(), name='register'),
    path('profile/', views.Profile.as_view(), name='profile')
]
