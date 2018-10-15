from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def user_new(request):
    if request.method != 'POST':
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})
    form = UserCreationForm(request.POST)
    if not form.is_valid():
        return render(request, 'registration/signup.html', {'form': form})
    user = form.save()
    username = form.cleaned_data.get('username')
    raw_password = form.cleaned_data.get('password')
    login(request, user)
    return redirect('post_list')
    