class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class BookManager:
    def __init__(self, storage):
        self.storage = storage
        self.books = self.storage.load_books()

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.storage.save_books(self.books)

    def update_book(self, isbn, title=None, author=None):
        is_updated=False
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                self.storage.save_books(self.books)
                is_updated=True
               
        if(is_updated):
            print("Book updated.")
        else:
            print("Book does not exist")
      

    def delete_book(self, isbn):
        prev_count=len(self.books)
        self.books = [book for book in self.books if book.isbn != isbn]
        after_count=len(self.books)
        if(prev_count==after_count):
            print("Book does not exist")
        else:
            print("Book deleted")
        self.storage.save_books(self.books)

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

    def search_by_title(self, title):
        found_books = [book for book in self.books if book.title == title]
        if found_books:
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        else:
            print("No book found with that title.")

    def search_by_author(self, author):
        found_books = [book for book in self.books if book.author == author]
        if found_books:
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        else:
            print("No book found by that author.")

    def search_by_isbn(self, isbn):
        found_books = [book for book in self.books if book.isbn == isbn]
        if found_books:
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        else:
            print("No book found with that ISBN.")
