from django import forms

from .models import Post,Profile

from django.contrib.auth.forms import UserCreationForm

from pyuploadcare.dj.forms import ImageField

from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class PostForm(forms.ModelForm):
    photo = ImageField(label='')

    class Meta:
        model = Post
        fields = ('photo',)
        
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile             
        fields = ['image']
              
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
