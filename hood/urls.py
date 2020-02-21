"""hood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include

from django.contrib import admin

from hoodie import views

from hoodie import views as hoodie_views

from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('hoodie/', include('hoodie.urls')),
    
    path('', views.home, name='home'),
    
    path('register/', hoodie_views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    
]
