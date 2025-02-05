from uuid import uuid4
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Book, Review

# Create your tests here.
class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_book = Book.objects.create(title='War and Peace', author='Leo Tolstoy', price='25.00')
        cls.user = get_user_model().objects.create_user(
            username='testuser', 
            email='testuser@email.com',
            password='testpass123'
        )
        cls.review = Review.objects.create(
            book = cls.test_book,
            author = cls.user,
            review = 'An excellent book'
        )

    def test_book_listing(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'War and Peace')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(reverse('book_detail', args=[str(self.test_book.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'War and Peace')
        self.assertContains(response, 'An excellent book')
        self.assertTemplateUsed(response, 'books/book_detail.html')

    def test_book_detail_view_not_found(self):
        # Use valid UUID format instead of 'a1b2c3'
        response = self.client.get(
            reverse('book_detail', 
            args=[str(uuid4())])  # Generate random valid UUID
        )
        self.assertEqual(response.status_code, 404)
    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertContains(response, 'War and Peace')