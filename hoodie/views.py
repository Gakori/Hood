from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from .forms import UserRegisterForm

from django.contrib import messages

def home(request):
    return HttpResponse('kjhgfcdgh')
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})
