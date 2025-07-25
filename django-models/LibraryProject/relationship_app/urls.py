from atexit import register

from django.contrib.auth.views import LoginView
from django.urls import path
from pyasn1_modules.rfc7906 import Register

from .views import list_books, LibraryDetailView, login_view, logout_view, register_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView, name='library_detail'),
    path('login/', login_view,  name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
