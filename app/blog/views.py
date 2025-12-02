from django.shortcuts import render
from .models import Post, Author, Comment

def index(request):
    post_num = Post.objects.count()
    author_num = Author.objects.count()
    comment_num = Comment.objects.count()

    latest_posts = Post.objects.order_by('-created_at')[:3]
    
    context = {
        'post_num': post_num,
        'author_num': author_num,
        'comment_num': comment_num,
        'latest_posts': latest_posts,
    }
    
    return render(request, 'blog/index.html', context)
