# QR_code_backend/urls.py

from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth
from app_blog import views as app_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_blog.urls')),
    path('login/', app_view.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('register/', app_view.register, name='register'),
]
