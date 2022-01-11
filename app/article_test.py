import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("techcrunch","Anna Heim","Hurricane Dorian","MOSTLY AI raises $25 million to further commercialize synthetic data in Europe and the U.S. – TechCrunch","Synthetic data startup MOSTLY raised a $25 million Series B round led by British VC firm Molten Ventures, with participation from new investor Citi Ventures and existing investors 42CAP and Earlybird.","https://techcrunch.com/wp-content/uploads/2021/11/GettyImages-1343238867.jpg?w=759","2022-01-11T09:03:39Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
    unittest.main()