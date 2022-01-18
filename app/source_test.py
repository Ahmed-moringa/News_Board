import unittest
from models import news

Sources = news.Sources

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Sources('abc-news-au','ABC News (AU)', 'Australia\'s most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.',"http://www.abc.net.au/news","news")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Sources))

if __name__ == '__main__':
    unittest.main()