from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import User , About # Import your User model
from django.shortcuts import render
from .forms import  UserForm, LoginForm, ContactForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



def home(request):
    users = User.objects.all()  # Get all users
    
    # Define the number of items per page
    items_per_page = 7 # Adjust this to your desired number of users per page

    paginator = Paginator(users, items_per_page)
    page = request.GET.get('page')

    try:
        paged_users = paginator.get_page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        paged_users = paginator.get_page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page of results.
        paged_users = paginator.get_page(paginator.num_pages)

    context = {
        'users': paged_users,
    }

    return render(request, "home.html", context)

class UserDetailView(DetailView):
    model = User
    template_name = 'cmdetails.html'  
    context_object_name = 'user'

def about(request):
     abouts= About.objects.all()
     context={
        'abouts':abouts
    }
     return render(request, 'about.html', context)

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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('home')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create a new Contact instance and save it to the database
            contact = form.save()
            # You can add any additional logic here, such as sending email notifications
            return redirect('home')  # Redirect to a success page
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def search(request):
    users = []  # Initialize with an empty queryset
    users_count = 0 
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            users = User.objects.filter(Q(first_name__icontains=keyword) | Q(PPA=keyword))
            users_count=users.count()
    context = {
        'users': users,
        'users_count':users_count
    }

    return render(request, 'search.html', context)
