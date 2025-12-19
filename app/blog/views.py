from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Author, Comment, Category

@login_required
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


def post_list(request):
    posts = Post.objects.order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-created_at')

    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'blog/post_detail.html', context)


def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'blog/category_list.html', context)