from django.urls import path

from . import views

from .views import PostCreateView

urlpatterns = [
    path('', views.home, name='home'),
    
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]
