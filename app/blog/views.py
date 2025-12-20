from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author, Comment, Category
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


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

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
        
            if request.user.is_authenticated:
                comment.author = request.user
                comment.author_name = ""
            else:
                if not comment.author_name:
                    form.add_error('author_name', "Вкажіть імʼя")
                    return render(request, 'blog/post_detail.html', {
                        'post': post,
                        'comments': comments,
                        'form': form,
                    })
        
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()

    is_moderator = False
    if request.user.is_authenticated:
        is_moderator = (
                request.user.is_superuser or
                request.user.groups.filter(name='Moderator').exists()
        )

    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'is_moderator': is_moderator,
    }
    return render(request, 'blog/post_detail.html', context)


def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'blog/category_list.html', context)


@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    user = request.user
    is_moderator = (
            user.is_superuser or
            user.groups.filter(name='Moderator').exists()
    )

    # перевірка прав
    if comment.author and comment.author != request.user and not is_moderator:
        return HttpResponseForbidden("Ви не маєте прав редагувати цей коментар")

    if request.method == 'POST':
        comment.text = request.POST.get('text')
        comment.save()
        return redirect('post-detail', pk=comment.post.pk)

    return render(request, 'blog/comment_edit.html', {'comment': comment})
