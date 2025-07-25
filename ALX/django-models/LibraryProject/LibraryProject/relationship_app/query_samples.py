from relationship_app.models import Author, Book, Relationship, Library, Librarian

def books_by_author(author):
    try:
        return Book.objects.filter(name=author)
    except Book.DoesNotExist:
        return []

def authors_by_book(book):
    try:
        return Book.objects.filter(book=book)
    except Book.DoesNotExist:
        return []

def authors_by_library(library):
    try:
        return Library.objects.filter(library=library)
    except Library.DoesNotExist:
        return []

def librarians_by_library(library):
    try:
        return Library.objects.filter(library=library)
    except Library.DoesNotExist:
        return []

def library_by_librarian(library):
    try:
        return Library.objects.filter(library=library)
    except Library.DoesNotExist:
        return []

def books_by_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

if __name__ == '__main__':
    print("Books by author 'John Doe':", books_by_author("John Doe"))
    print("Books in library 'Central Library':", books_in_library("Central Library"))
    print("Librarian of 'Central Library':", librarian_of_library("Central Library"))