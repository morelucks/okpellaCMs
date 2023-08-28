from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import User  # Import your User model

def home(request):
    users= User.objects.all()
    context={
        'users':users
    }
    return render(request, "home.html", context)

class UserDetailView(DetailView):
    model = User
    template_name = 'cmdetails.html'  
    context_object_name = 'user'


