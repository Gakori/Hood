from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from django.views.generic import ListView, CreateView

from .forms import UserRegisterForm, PostForm

from django.contrib import messages

from django.urls import reverse_lazy

from .models import Post

def home(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = PostForm()

    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None 
        
    return render(request, 'hoodie/home.html', { 'posts': posts, 'form': form })

class PostCreateView(CreateView):
    model = Post
    fields = ['name', 'description', 'location', 'photo']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
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
