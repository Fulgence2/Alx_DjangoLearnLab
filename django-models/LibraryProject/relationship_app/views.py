from django.views.generic.detail import DetailView
from aiohttp.web_urldispatcher import View
from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from .models import Librarian
from .models import Author
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm

# Create your views here.
from django.http import JsonResponse


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(View):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

#User registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(list_books)
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# User login view

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(list_books)
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# Logout

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')


# Password change

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'relationship_app/password_change.html')
    else:
        form = PasswordChangeForm()
    return render(request, 'relationship_app/password_change.html', {'form': form})