from django.urls import path
from .import views 
from .views import UserDetailView
urlpatterns = [
    path('', views.home, name = "home"),
    path('user/<int:pk>/', UserDetailView.as_view(), name='cmdetails'),
]