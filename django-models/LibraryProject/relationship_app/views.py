from msilib.schema import ListView

from aiohttp.web_urldispatcher import View
from django.shortcuts import render
from .models import Book
from .models import Library
from .models import Librarian
from .models import Author

# Create your views here.
from django.http import JsonResponse

from LibraryProject.bookshelf.models import Book


def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(View):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'