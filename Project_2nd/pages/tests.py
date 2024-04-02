from django.test import TestCase

# Create your tests here.
class SimpleTests(TestCase):
    def test_home_page(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_about_page(self):
        res = self.client.get('/')

        print(str(res))
        return self.assertEqual(res.status_code, 200)    