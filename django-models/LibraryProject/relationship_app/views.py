from django.views.generic.detail import DetailView
from aiohttp.web_urldispatcher import View
from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from .models import Librarian
from .models import Author
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import login
from django.http import HttpResponseForbidden
from .models import Book, Author
from .forms import BookForm

# Create your views here.
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test


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



# Helper functions to check roles
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

#Add book

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_books)
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form, 'action': 'add_book'})


#Edit Book
@permission_required('relationship_app.can_edit_book', raise_exception=True)
def edit_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, instance=Book)
        if form.is_valid():
            form.save()
            return redirect(list_books)
    else:
        form = BookForm(instance=Book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'action': 'edit_book'})


#Delete book

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, instance=Book)
        if form.is_valid():
            form.save()
            return redirect(list_books)
    else:
        form = BookForm(instance=Book)
    return render(request, 'relationship_app/delete_book.html', {'form': form, 'action': 'delete_book'})