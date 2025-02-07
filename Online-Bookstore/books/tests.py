from uuid import uuid4
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
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
        cls.special_permission = Permission.objects.get(codename='special_status')
        cls.review = Review.objects.create(
            book = cls.test_book,
            author = cls.user,
            review = 'An excellent book'
        )

    def test_book_listing(self):
        self.client.login(username='testuser', password='testpass123')  
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'War and Peace')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view_for_logged_in_user(self):
        self.client.login(username='testuser', password='testpass123')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(reverse('book_detail', args=[str(self.test_book.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'War and Peace')
        self.assertContains(response, 'An excellent book')
        self.assertTemplateUsed(response, 'books/book_detail.html')

    def test_book_detail_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('book_detail', args=[str(self.test_book.id)]), follow=True)
        
        # Check that a redirect occurred
        self.assertTrue(response.redirect_chain)
        
        # Assert the first redirect is to the expected login URL
        expected_redirect = f'/accounts/login/?next=/books/{self.test_book.id}/'
        # redirect_chain is a list of tuples (redirect_url, status_code)
        self.assertEqual(response.redirect_chain[0][0], expected_redirect)
        
        # Finally, verify that the final page contains the login content
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Log In')


    def test_book_detail_view_with_special_permission(self):
        self.client.login(username='testuser', password='testpass123')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(reverse('book_detail', args=[str(self.test_book.id)]))
        no_response = self.client.get('/books/a1b2c3d4-a1b2-a1b2-a1b2-a1b2c3d4e5/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'War and Peace')
        self.assertContains(response, 'An excellent book')
        self.assertTemplateUsed(response, 'books/book_detail.html')

    def test_book_detail_view_not_found(self):
        self.client.login(username='testuser', password='testpass123')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(
            reverse('book_detail', 
            args=[str(uuid4())])  # Generate random valid UUID
        )
        self.assertEqual(response.status_code, 404)

    def test_book_list_view(self):
        self.client.login(username='testuser', password='testpass123')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertContains(response, 'War and Peace') 