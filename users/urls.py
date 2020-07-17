from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='gleo-signup'),
    path('profile/', views.profile, name='user-profile'),
]