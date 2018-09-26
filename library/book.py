class Book():
    def __init__(self, title, author, publication, publication_year, isbn, total_book):
        self.title = title
        self.author = author
        self.publication = publication
        self.publication_year = publication_year
        self.isbn = isbn
        self.total_book = total_book

    def getTitle(self):
        return self.titile

    def getAuthor(self):
        return self.author

    def getPublication(self):
        return self.publication

    def getPublicationYear(self):
        return self.publication_year

    def getISBN(self):
        return self.isbn

    def getTotalBook(self):
        return self.total_book

    def setTitle(self, title):
        self.title = title

    def setAuthor(self, author):
        self.author = author

    def setPublication(self, publication):
        self.publication = publication

    def setPublicationYear(self, publication_year):
        self.publication_year = publication_year

    def setISBN(self, isbn):
        self.isbn = isbn

    def setTotalBook(self, total_book):
        self.total_book = total_book
