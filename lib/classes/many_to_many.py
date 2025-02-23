class Article:
    def __init__(self, author, magazine, title):
        # Initialize with author, magazine, and title
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters long.")
        
        self._author = author
        self._magazine = magazine
        self._title = title  # Use a private attribute for title
        self._author.add_article(self)  # Associate this article with the author



    @property
    def title(self):
        # Returns the title of the article
        return self._title

    @title.setter
    def title(self, value):
        # Prevent modification of the title
        raise AttributeError("Title is immutable and cannot be modified.")

    @property
    def author(self):
        # Returns the author of the article
        return self._author

    @author.setter
    def author(self, value):
        # Allow changing the author (must be of type Author)
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of the Author class.")
        self._author = value

    @property
    def magazine(self):
        # Returns the magazine of the article
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        # Allow changing the magazine (must be of type Magazine)
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")
        self._magazine = value



class Author:
    def __init__(self, name):
        # Ensure name is a string and its length is greater than 0
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        
        self._name = name  # Use a private attribute to store the name
        self._articles = []

    @property
    def name(self):
        # Returns the author's name
        return self._name

    @name.setter
    def name(self, value):
        # Prevent modification of the name after instantiation
        raise AttributeError("Name is immutable and cannot be modified.")
    def articles(self):
        """Returns a list of all articles written by the author"""
        return self._articles

    def magazines(self):
        """Returns a unique list of magazines the author has written for"""
        unique_magazines = {article.magazine for article in self._articles}
        return list(unique_magazines)

    def add_article(self, magazine, title):
        """Adds an article to the author's list of articles"""
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

        
    def topic_areas(self):
        if not self._articles:
            return None
        unique_categories = {article.magazine.category for article in self._articles}
        return list(unique_categories)

class Magazine:
    def __init__(self, name, category):
        # Validate the name to ensure it's a string and between 2 and 16 characters
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters long.")
        
        # Validate the category to ensure it's a string and has length > 0
        if not isinstance(category, str):
            raise TypeError("Category must be a string.")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters.")
        
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
            raise TypeError("Name must be a string.")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters long.")
        
        self._name = value  # Update the magazine's name

    @property
    def category(self):
        # Returns the magazine's category
        return self._category

    @category.setter
    def category(self, value):
        # Ensure the new category is valid
        if not isinstance(value, str):
            raise TypeError("Category must be a string.")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters.")
        
        self._category = value  # Update the magazine's category
    def add_article(self, article):
        """Adds an article to the magazine's list of articles"""
        if isinstance(article, Article):
            self._articles.append(article)
        else:
            raise TypeError("Expected an Article instance.")

    
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
        if not self._articles:
            return None
        
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        # Filter authors with more than 2 articles
        return [author for author, count in author_counts.items() if count > 2]



  