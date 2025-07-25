from relationship_app.models import Author, Book, Relationship, Library, Librarian

def books_by_author(author):
    try:
        author = ["Author.objects.get(name=author_name)", "objects.filter(author=author)"]
        return Book.objects.filter(author__in=author)
    except Book.DoesNotExist:
        return []

def authors_by_book(book):
    try:
        book = ["Book.objects.get(name=book_name)", "objects.filter(book=book)"]
        return Book.objects.filter(book__in=book)
    except Book.DoesNotExist:
        return []

def authors_by_library(library):
    try:
        library = ["Library.objects.get(name=library_name)", "objects.filter(library=library)"]
        return Library.objects.filter(library__in=library)
    except Library.DoesNotExist:
        return []

def librarians_by_library(library):
    try:
        library = ["Library.objects.get(name=library_name)", "objects.filter(library=library)"]
        return Library.objects.filter(library__in=library)
    except Library.DoesNotExist:
        return []

# === Query 3: Retrieve the librarian for a specific library ===
def librarian_of_library(library_name):
    try:
        # Get the librarian directly via the related OneToOneField
        library = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=library)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []


if __name__ == '__main__':
    print("Books by author 'John Doe':", books_by_author("John Doe"))
    print("Books in library 'Central Library':", books_by_library("Central Library"))
    print("Librarian of 'Central Library':", librarian_by_library("Central Library"))
