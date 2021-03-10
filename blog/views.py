from django.shortcuts import render, get_object_or_404, redirect, reverse
from blog.models import Post, Comment
from blog.forms import NewComment, CreatePostForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    posts = Post.objects.all().order_by('-post_date')

    paginator = Paginator(posts, 4)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'title': 'الصفحة الرئيسية',
        'posts': posts,
        'page': page
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
            CommentForm = CommentForm.save(commit=False)
            CommentForm.post = post
            CommentForm.save()
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


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    form_class = CreatePostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    form_class = CreatePostForm



    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class DeletePost(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
