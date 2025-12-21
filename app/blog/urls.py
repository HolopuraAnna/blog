from django.urls import path
from . import views
from .api_views import PostListAPIView

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post-list'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('categories/', views.category_list, name='category_list'),
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment-edit'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment-delete'),
    path('api/posts/', PostListAPIView.as_view(), name='api-posts'),
]
