from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.userlogin, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.userlogout, name='logout'),
]