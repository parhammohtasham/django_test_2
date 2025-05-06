from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class PostTestList(TestCase):
    def setUp(self):
        Post.objects.create(text='hello')
    def test_setUp(self):
        posts=Post.objects.get(id=1)
        except_object_name=f'{posts}'
        self.assertEqual(except_object_name,'hello')
    def test_post_string_model(self):
        post=Post(text='hello')
        self.assertEqual(str(post),post.text)

class PostTestView(TestCase):
    def test_post_list_view(self):
        response=self.client.get(reverse('posts'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'posts/list.html')

    def test_post_new_view(self):
        response=self.client.get(reverse('new_post'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'posts/new.html')