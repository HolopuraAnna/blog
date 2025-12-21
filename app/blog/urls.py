from django.urls import path
from . import views
from .api_views import PostListAPIView
from .api_views import PostListCreateAPIView, PostDetailAPIView, CommentListCreateAPIView, CommentDetailAPIView


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post-list'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('categories/', views.category_list, name='category_list'),
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment-edit'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment-delete'),
    path('api/posts/', PostListAPIView.as_view(), name='api-posts'),
    # REST API
    path('api/posts/', PostListCreateAPIView.as_view(), name='api-post-list'),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name='api-post-detail'),
    path('api/posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='api-comment-list'),
    path('api/comments/<int:pk>/', CommentDetailAPIView.as_view(), name='api-comment-detail'),
]
