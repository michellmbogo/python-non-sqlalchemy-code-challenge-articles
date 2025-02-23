class Author:
    def __init__(self, name):
        # Ensure name is a non-empty string
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []  # List to store articles written by the author

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles  # Return a list of articles written by the author

    def magazines(self):
        # Return a unique list of magazines the author has contributed to
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        # Ensure name is between 2 and 16 characters, and category is a non-empty string
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        
        self._name = name
        self._category = category
        self._articles = []  # List to store articles published in the magazine

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category

    def articles(self):
        return self._articles  # Return all articles in the magazine

    def contributors(self):
        return list(set(article.author for article in self._articles))  # Unique authors who contributed

    def add_article(self, article):
        self._articles.append(article)

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors_with_more_than_two = [
            author for author in self.contributors() 
            if len([article for article in self._articles if article.author == author]) > 2
        ]
        return [author.name for author in authors_with_more_than_two] if authors_with_more_than_two else None


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Article title must be between 5 and 50 characters.")
        
        self._author = author  # Author instance
        self._magazine = magazine  # Magazine instance
        self._title = title  # Article title

    @property
    def title(self):
        return self._title  # Title is immutable after creation

    @property
    def author(self):
        return self._author  # Author of the article (immutable)

    @property
    def magazine(self):
        return self._magazine  # Magazine of the article (mutable)

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine.")
        self._magazine = new_magazine  # Allow the magazine to change if needed
