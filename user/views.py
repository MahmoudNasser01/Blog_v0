from django.shortcuts import render, redirect
from user.forms import UserCreationForm
from django.contrib import messages


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, 'تهانينا لقد تمت عمليه التسجيل بنجاح')
            return redirect('home')
    else:
        form = UserCreationForm()
    context = {
        'title': 'التسجيل في المدونة',
        'form': form
    }
    return render(request, 'user/register.html', context)
