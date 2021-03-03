from django.shortcuts import render, get_object_or_404,redirect, reverse
from blog.models import Post, Comment
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

    if request.method == 'POST':
        CommentForm = NewComment(request.POST)
        if CommentForm.is_valid():
            new_comment = CommentForm.save(commit=False)
            new_comment.post = post
            new_comment.save()
            CommentForm = NewComment()
            return redirect(reverse('detail', args=(post_id,)))

    else:
        CommentForm = NewComment()


    comments = post.comments.all()
    context = {
            'title': 'title_for_now',
            'post': post,
            'comments': comments,
            'CommentForm': CommentForm
        }




    return render(request, 'blog/detail.html', context)
