from django.contrib import admin
from django.urls import path
from . import views

app_name='account'
urlpatterns = [
    path('login/',views.login_page , name='login'),
    path('register/',views.register_page ,name='register'),
    path('home/',views.home_view, name='home'),
    path('logout/',views.logout_view, name='logout'),

]
