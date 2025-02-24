class Article:
    all = []  
    def __init__(self, author, magazine, title):
    
        # The article is added to  the author, magazine and class level list
        if self not in author.articles():
            author.articles().append(self)

        if self not in magazine.articles():
            magazine.articles().append(self)

        if self not in Article.all:
            Article.all.append(self)

        self.author = author
        self.magazine = magazine
        self.title = title  


    @property
    def author(self):
        """author of the article."""
        return self._author

    @author.setter
    def author(self, value):
        
        if not isinstance(value, Author):
            raise ValueError("Author must be of type Author.")
        self._author = value

    @property
    def magazine(self):
        """Returns the magazine where the article is published."""
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be of type Magazine.")
        self._magazine = value


    @property
    def title(self):
        """ article's title."""
        return self._title

    @title.setter
    def title(self, value):
        
        if not isinstance(value, str):
            return  
        if len(value) < 5 or len(value) > 50:
            return  
        if hasattr(self, "_title"):
            return 
        self._title = value

class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []  


    def magazines(self):
        """Returns a unique list of magazines the author has contributed to."""
        return list(set(article.magazine for article in self._articles))

    @property
    def name(self):
        """Returns the author's name."""
        return self._name

    @name.setter
    def name(self, value):
        
        if not isinstance(value, str):
            return  
        if len(value) == 0:
            return  
        if hasattr(self, "_name"):
            return  
        self._name = value

    def articles(self):
        """Returns a list of all articles written by the author."""
        return self._articles

    def add_article(self, magazine, title):
        
        new_article = Article(self, magazine, title)
        return new_article  
    def topic_areas(self):
        
        if not self._articles:
            return None
        return list(set(magazine.category for magazine in self.magazines()))






class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []  # List to store articles published in the magazine
    

    @property
    def category(self):
        """ magazine's category."""
        return self._category

    @category.setter
    def category(self, value):
        
        if not isinstance(value, str):
            return  
        if len(value) == 0:
            return  
        self._category = value

    def articles(self):
        """list of all articles published in the magazine."""
        return self._articles
    
    def article_titles(self):
        
        if not self._articles:
            return None
        return [article.title for article in self._articles]


    @property
    def name(self):
        """ magazine's name."""
        return self._name

    @name.setter
    def name(self, value):
        
        if not isinstance(value, str):
            return  
        if len(value) < 2 or len(value) > 16:
            return  
        self._name = value

    def contributors(self):
        
        return list(set(article.author for article in self._articles))

    def contributing_authors(self):
        """
        Returns a list of authors who have written more than 2 articles for the magazine.
        """
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        return [author for author, count in author_counts.items() if count > 2] or None