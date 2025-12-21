from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
