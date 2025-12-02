from django.shortcuts import render
from .models import Post, Author, Comment

def index(request):
    post_num = Post.objects.count()
    author_num = Author.objects.count()
    comment_num = Comment.objects.count()
    
    context = {
        'post_num': post_num,
        'author_num': author_num,
        'comment_num': comment_num,
    }
    
    return render(request, 'blog/index.html', context)
