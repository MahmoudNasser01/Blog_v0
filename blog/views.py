from django.shortcuts import render, get_object_or_404
from blog.models import Post,Comment
from blog.forms import NewComment




def home(request):
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': Post.objects.all().order_by('-post_date'),
    }
    return render(request, 'blog/index.html', context)


def about(request):
    context = {
        'title': 'من انا'
    }
    return render(request, 'blog/about.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    CommentForm = NewComment()

    context = {
        'title': 'title_for_now',
        'post': post,
        'comments': post.comments.filter(active=True).order_by('-comment_date'),
        'CommentForm': CommentForm
    }
    return render(request, 'blog/detail.html', context)

