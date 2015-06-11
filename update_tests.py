import unittest
import urllib2

from bs4 import BeautifulSoup
from urlparse import urljoin


class RetrieveTest(unittest.TestCase):
    BASE_URL = 'http://reutilitza.cat'
    VERBOSE = False
    
    def get_url(self, path):
        url = urljoin(self.BASE_URL, path)
        response = urllib2.urlopen(url)
        
        if self.VERBOSE:
            print(response.getcode())
            print(response.info())
        
        return response
    
    def get_title(self, content):
        # http://www.crummy.com/software/BeautifulSoup/bs4/doc/
        soup = BeautifulSoup(content)
        return soup.title.string
        
    def test_root(self):
        response = self.get_url('/')
        self.assertEqual(200, response.getcode())
        
        title = self.get_title(response.read())
        self.assertEqual('Projectes socials | reutilitza.cat', title)


if __name__ == '__main__':
    unittest.main()
