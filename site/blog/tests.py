from django.test import TestCase
from .models import Blog
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.

class BlogEditView(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='Mohammad',
            password='1234'
        )
        self.blog=Blog.objects.create(
            title='blog title',
            body='blog body',
            author=self.user)
      
    def test_setUp(self):
        self.assertEqual(f'{self.blog.title}','blog title')
        self.assertEqual(f'{self.blog.body}','blog body')
        self.assertEqual(f'{self.blog.author}','Mohammad')

    def test_blog_string_model(self):
        blog=Blog(title='hello world!')
        self.assertEqual(f'{blog}',blog.title)

    def test_blog_list_view(self):
        response=self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'blog/list.html')

    def test_blog_detail_view(self):
        response=self.client.get('/blogs/1/')
        no_response=self.client.get('/blogs/10/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertTemplateUsed(response,'blog/detail.html')

    def test_get_absolute_url(self):
        self.assertEqual(self.blog.get_absolute_url(),'/blogs/1/')

    def test_create_blog(self):
        response=self.client.post(reverse('blog_new'),{
            'title':'new post',
            'body':'new body',
            'author':self.user.id,
        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(Blog.objects.last().title,'new post')
        self.assertEqual(Blog.objects.last().body,'new body')

    def test_update_blog(self):
        response=self.client.post(reverse('blog_update',args='1'),{
            'title':'updated title',
            'body':'updated body',
        })
        self.assertEqual(response.status_code,302)

    def test_delete_Blog(self):
        response=self.client.post(reverse('blog_delete',args='1'))
        self.assertEqual(response.status_code,302)