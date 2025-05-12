from django.urls import path
from .views import (PostListView, UserPostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
                    like_post, add_comment)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),    
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('like/<int:post_id>/', views.like_post, name='like-post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add-comment'),
    path('about/', views.about, name='blog-about'),
]