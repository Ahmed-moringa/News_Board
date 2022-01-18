class Articles:
    """ 
    Article class to define Article Objects
    
    """
    def __init__(self,author,title,description,url,urlToImage,publishedAt):

        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage= urlToImage
        self.publishedAt = publishedAt

class Sources:
    """ 
    Sources class to define news source objects
    """

    def __init__(self, id, name, description, url, category):
        
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
