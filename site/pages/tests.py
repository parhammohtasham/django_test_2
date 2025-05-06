from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class PageTestView(TestCase):
    def test_home_page_view(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response , 'pages/home.html')