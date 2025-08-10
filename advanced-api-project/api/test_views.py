from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book


class AuthorBookAPITests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Author 1")
        self.book = Book.objects.create(
            title="Book 1",
            publication_year=2024,
            author=self.author
        )

    def test_get_authors_list(self):
        url = reverse('author-list')  # Adjust to your actual route name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_author(self):
        url = reverse('author-detail', args=[self.author.id])  # Adjust route name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_books_list(self):
        url = reverse('book-list')  # Adjust route name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_book(self):
        url = reverse('book-detail', args=[self.book.id])  # Adjust route name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BookListViewTest(APITestCase):
    def test_book_list_view(self):
        author = Author.objects.create(name="Test Author")
        Book.objects.create(
            title="Test Book",
            author=author,  # ✅ Pass the Author instance
            publication_year=2024
        )
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('title', response.data[0])  # ✅ Uses response.data