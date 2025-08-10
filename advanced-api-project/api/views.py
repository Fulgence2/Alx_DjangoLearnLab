from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book
from .serializers import BookSerializer
from rest_framework import generics
from .serializers import AuthorSerializer

# List all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Get details of a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPITests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Author 1")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2023,
            author=self.author
        )

    def test_get_all_books(self):
        url = reverse('book-list')  # You need to make sure this matches your urls.py name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_single_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_get_non_existent_book(self):
        url = reverse('book-detail', kwargs={'pk': 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UserAPITests(APITestCase):

    def setUp(self):
        # Create a sample user
        self.user = Author.objects.create(name="Another Author")
        self.book = Book.objects.create(
            title="Another Test Book",
            publication_year=2024,
            author=self.user
        )

    def test_get_users_list(self):
        url = reverse('user-list')  # Make sure this matches your urls.py name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
