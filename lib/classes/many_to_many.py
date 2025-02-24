class Article:
    def __init__(self, author, magazine, title):
        # Initialize with author, magazine, and title
        if self not in author.articles():
            author.articles().append(self)

        if self not in magazine.articles():
            magazine.articles().append(self)

        if self not in Article.all:
            Article.all.append(self)

        self._author = author
        self._magazine = magazine
        self._title = title  # Use a private attribute for title
        
    @property
    def title(self):
        # Returns the title of the article
        return self._title

    @title.setter
    def title(self, value):
        # Prevent modification of the title
        if not isinstance(value, str):
            return  # Ignore non-string assignments without any feedback
        if len(value) < 5 or len(value) > 50:
            return
        if hasattr(self, "_title"):
            return
        self._title = value  # Assign title only if it's within valid length and not previously set

    @property
    def author(self):
        # Returns the author of the article
        return self._author

    @author.setter
    def author(self, value):
         
         if type(value,Author): 
         raise ValueError("Author must be of type Author.")
         self._author = value

    @property
    def magazine(self):
        # Returns the magazine of the article
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
        raise ValueError("Expected value to be an instance of the Magazine class.")
        self._magazine = value


class Author:
    def __init__(self, name):
    
        self._name = name  # Use a private attribute to store the name
        self._articles = []

    @property
    def name(self):
        # Returns the author's name
        return self._name

    @name.setter
    def name(self, value):
        # Ensure name is a string and its length is greater than 0
        if not isinstance(value, str):
            return
        if len(value) == 0:
            return
        if hasattr(self, "_name"):
            return
        self._name = value  # Use a private attribute to store the name
        
    @property
    def articles(self):
        """Returns a list of all articles written by the author"""
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))


    def add_article(self,magazine, title):
        """Adds an article to the author's list of articles"""
        new_article = Article(self, magazine, title)
        return new_article 

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(magazine.category for magazine in self.magazines()))

class Magazine:
    def __init__(self, name, category):
        # # Validate the name to ensure it's a string and between 2 and 16 characters
        # if not isinstance(name, str):
        #     raise TypeError("Name must be a string.")
        # if not (2 <= len(name) <= 16):
        #     raise ValueError("Name must be between 2 and 16 characters long.")
        
        # # Validate the category to ensure it's a string and has length > 0
        # if not isinstance(category, str):
        #     raise TypeError("Category must be a string.")
        # if len(category) == 0:
        #     raise ValueError("Category must be longer than 0 characters.")
        
        self._name = name  # Use a private variable to store the name
        self._category = category  # Use a private variable to store the category
        self._articles = []

    @property
    def name(self):
        # Returns the magazine's name
        return self._name

    @name.setter
    def name(self, value):
        # Ensure the new name is valid
        if not isinstance(value, str):
            return
        if len(value) < 2 or len(value) > 16:
            return 
        self._name = value  # Update the magazine's name

    @property
    def category(self):
        # Returns the magazine's category
        return self._category

    @category.setter
    def category(self, value):
        # Ensure the new category is valid
        if not isinstance(value, str):
            return
        if len(value) == 0:
            return
        self._category = value  # Update the magazine's category

    # def add_article(self, article):
    #     """Adds an article to the magazine's list of articles"""
    #     if isinstance(article, Article):
    #         self._articles.append(article)
    #     else:
    #         raise TypeError("Expected an Article instance.")

    @property
    def articles(self):
        """Returns a list of all articles in the magazine"""
        return self._articles

    def article_titles(self):
        """Returns a list of titles of all articles in the magazine"""
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributors(self):
        """Returns a list of authors who have contributed to the magazine"""
        return list({article.author for article in self._articles})

    def contributing_authors(self):
        """Returns a list of authors who have written more than 2 articles"""
        # if not self._articles:
        #     return None
        
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        # Filter authors with more than 2 articles
        return [author for author, count in author_counts.items() if count > 2]
