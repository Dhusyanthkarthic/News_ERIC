import unittest
from App import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertIn(b"<h1>Headlines</h1>", response.data)
        

    def test_news_articles_for_keyword(self):
        response = self.client.post('/', data={'keyword': 'technology'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Technology", response.data)
        
    def test_keyword_search_template(self):
        response = self.client.post('/', data={'keyword': 'politics'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<!DOCTYPE html>", response.data)
      
if __name__ == '__main__':
    unittest.main()
