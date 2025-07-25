from atexit import register
from tempfile import template
from . import views
from django.contrib.auth.views import LoginView
from django.urls import path
from pyasn1_modules.rfc7906 import Register

from .views import list_books, LibraryDetailView, login_view, logout_view, register_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView, name='library_detail'),
    #Auth Views
    path('register/', views.register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    # Book actions with permissions
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]
