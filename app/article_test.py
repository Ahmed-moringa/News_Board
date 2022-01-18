
import unittest
from models import news

Articles = news.Articles

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles("Riley","Hurricane Dorian","The storm has left at least 43 dead","http//www.vox.com","https://www.thehindu.com/static/theme/default/base/img/og-image.jpg","2019-09-07T19:41:51Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

if __name__ == '__main__':
    unittest.main()