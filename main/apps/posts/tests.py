from django.test import TestCase
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    def setup(self):
        Post.objects.create(title='test case')
        Post.objects.create(text='text case')
    
    def test_fields(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        expected_text = f'{post.text}'
        self.assertEqual(expected_title,'test case')
        self.assertEqual(expected_text,'test case')
        