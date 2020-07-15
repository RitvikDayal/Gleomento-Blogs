from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gleo-home'),
    path('blog/', views.blog, name='gleo-blog'),
    path('about/', views.about, name='gleo-about'),
]