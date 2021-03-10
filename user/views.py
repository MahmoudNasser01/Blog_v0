from django.shortcuts import render, redirect
from user.forms import SignUpForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from blog.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تهانينا لقد تمت عمليه التسجيل بنجاح')
            return redirect('login')
    else:
        form = SignUpForm()
    context = {
        'title': 'التسجيل في المدونة',
        'form': form
    }
    return render(request, 'user/register.html', context)


def login_user(request):
    form = LoginForm()

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'هناك خطاء في اسم المستخدم او كلمة المرور')

    context = {
        'title': 'تسجيل دخول',
        'form': form
    }
    return render(request, 'user/login.html', context)


@login_required(login_url='/login')
def profile(request):
    posts = Post.objects.filter(author=request.user)
    post_list = Post.objects.filter(author=request.user)
    paginator = Paginator(posts, 1)

    page = request.GET.get('page')

    try:
        post_list = paginator.page(page)

    except PageNotAnInteger:
        post_list = paginator.page(1)

    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context = {
        'title': 'الملف الشخصي',
        'posts': posts,
        'page': page,
        'post_list':post_list
    }
    return render(request, 'user/profile.html', context)


@login_required(login_url='/login')
def ProfileUpdate(request):

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, 'تم التعديل بنجاح')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)



    context = {
        'title': 'تعديل الملف الشخصي',
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'user/profile_update.html', context)