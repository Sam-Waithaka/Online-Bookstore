from django.test import SimpleTestCase
from django.urls import resolve, reverse

from .views import HomePageView, AboutPageView

class HomePageTests(SimpleTestCase):
    url = '/'
    view = HomePageView
    template = 'home.html'
    expected_text = 'Welcome to our Bookstore'
    unexpected_text = 'Hi there! I should not be on the page.'

    def setUp(self):
        self.response = self.client.get(self.url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, self.template)

    def test_homepage_url_name(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        self.assertContains(self.response, self.expected_text)

    def test_home_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, self.unexpected_text)

    def test_home_page_url_resolves_home_page_view(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            self.view.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):
    url = '/about/'
    view = AboutPageView
    template = 'about.html'
    expected_text = 'This is an online bookstore.'
    unexpected_text = 'Hi there! I should not be on the page.'

    def setUp(self):
        self.response = self.client.get(self.url)

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, self.template)

    def test_about_page_url_name(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response, self.expected_text)

    def test_about_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, self.unexpected_text)

    def test_about_page_url_resolves_about_page_view(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            self.view.as_view().__name__
        )