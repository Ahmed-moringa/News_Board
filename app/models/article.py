class Article:
    """ 
    Article class to define Article Objects
    
    """
    def __init__(self,name,author,title,description,url,urlToImage,publishedAt):

        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage= urlToImage
        self.publishedAt = publishedAt