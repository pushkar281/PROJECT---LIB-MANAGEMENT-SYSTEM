
from Book import Book

class Catalog:
    def __init__(self):
        self.different_book_count = 0
        self.books = []

    def addBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)
        self.different_book_count += 1
        self.books.append(b)
        return b

    def removeBook(self,inputName):
        for book in self.books:
            if inputName.strip() == book.name:
                self.books.remove(book)
                self.different_book_count -= 1

    def addBookItem(self,book,isbn,rack):
        book.addBookItem(isbn, rack)

    def searchByName(self,name):
        for book in self.books:
            if name.strip() == book.name:
                return book

    def searchByAuthor(self,author):
        for book in self.books:
            if author.strip() == book.author:
                return book

    def displayAllBooks(self):
        print ('Different Book Count',self.different_book_count)
        c = 0
        for book in self.books:
            c += book.total_count
            book.printBook()
        print ('Total Book Count',c)

    def removeBookItem(self,name,isbn):
        book = self.searchByName(name)
        book_item = book.searchBookItem(isbn)
        book.removeBookItem(book_item)
