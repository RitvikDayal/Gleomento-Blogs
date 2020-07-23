from django.urls import path
from .views import PostListView, UserPostListView, PostDetailView, PostCreateView,PostDeleteView, PostUpdateView
from . import views

urlpatterns = [
    path('', views.home, name='gleo-home'),
    path('blog/user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('blog/', PostListView.as_view(), name='gleo-blog'),
    path('blog/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('blog/post/new/', PostCreateView.as_view(), name='post-create'),
    path('blog/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='gleo-about'),
]