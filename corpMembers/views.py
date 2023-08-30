from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import User  # Import your User model
from django.shortcuts import render
from .forms import  UserForm

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



def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data
            form.save()
            return redirect('home') 
    else:
        form = UserForm()
    
    return render(request, 'register_form.html', {'form': form})
