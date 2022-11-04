from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from django.test import Client


class Bugs(TestCase):
    def test_xss(self):
        c = Client()
        response = self.client.get('/gift/?director=<script>alert("Vulnerable to XSS!")</script>', follow=True)
        print(response.content)
        #self.assertEqual(response.content, 200)
        response = c.get('/gift.html/?director=<script>alert("Vulnerable to XSS!")</script>')
        response.content