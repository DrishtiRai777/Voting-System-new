from django.contrib import admin
from django.urls import path
from backapp import views 



urlpatterns = [
    path('', views.main, name='home'),
    path('userlogin/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('org_login/', views.org_login, name='org_login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_up02/', views.sign_up02, name='sign_up02'),
    path('sign_up03/', views.sign_up03, name='sign_up03'),
    path('org_dashboard/', views.org_dashboard, name='org_dashboard'),
]
