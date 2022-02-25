from django.http.response import ResponseHeaders
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Blog
# Create your tests here.

class BlogTests(TestCase):
    def set_up(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@mail.com',
            password='secret',
        )
        self.blog = Blog.objects.create(
            title = 'A good title',
            body = 'Nice body content',
            author = self.user,
        )
    def test_string_representation(self):
        blogv = Blog(title='a sample title')
        self.assertEqual(str(blogv),self.blog.title)
    def test_blog_content(self):
        self.assertEqual(f'{self.blog.title}','A good title')
        self.assertEqual(f'{self.blog.body}','Nice body content')
        self.assertEqual('f{self.blog.author}','testuser')
    def test_blog_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response,'home.html')
    def test_blog_post_details(self):
        response = self.client.get('/blog/1')
        no_response = self.client.get('/blog/5')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'A good title')
        self.assertTemplateUsed(response,'detail.html')

    def test_get_absolute_url(self):
        self.assertEqual(self.blog.get_absolute_url(),'/blog/1')
    def test_blog_creat_view(self):
        pass
    def test_blog_update_view(self):
        pass
    def test_blog_del_view(self):
        pass
