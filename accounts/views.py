from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from .models import Profile
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You are now able to log in')
            return redirect('login')

    else:
        form = UserRegisterForm()

    context = {
        'form' : form
    }
    return render(request,'accounts/register.html', context)


def user_profile(request):
    return render (request,'accounts/user_profile.html')
