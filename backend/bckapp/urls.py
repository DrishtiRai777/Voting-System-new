from django.contrib import admin
from django.urls import path
from bckapp import views 

urlpatterns = [
    path('', views.main, name='home'),
    path('userlogin', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('org_login', views.org_login, name='org_login'),
    path('sign_up', views.sign_up, name='org_signup'),
    path('sign_up02', views.sign_up02, name='org_signup02'),
    path('sign_up03', views.sign_up03, name='org_signup03'),
]
