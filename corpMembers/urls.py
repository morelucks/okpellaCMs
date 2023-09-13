from django.urls import path
from .import views 
from .views import UserDetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = "home"),
    path('register/', views.register, name = "register"),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),

    path('contact/', views.contact, name='contact'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logoutUser, name="logout"),

    path('user/<int:pk>/', UserDetailView.as_view(), name='cmdetails'),
]