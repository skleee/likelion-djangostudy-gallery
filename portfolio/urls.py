from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:portfolio_id>/', views.detail, name="detail"),
    path('new/', views.new, name='new'),
    path('<int:portfolio_id>/edit/', views.edit, name="edit"),
    path('<int:portfolio_id>/delete/', views.delete, name="delete"),
]
