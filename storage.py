import os
import json
from book import Book
from user import User  

class BookEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return {'title': obj.title, 'author': obj.author, 'isbn': obj.isbn}
        elif isinstance(obj, User):
            return {'name': obj.name, 'user_id': obj.user_id}
        return super().default(obj)

class JSONStorage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                file.write('{}')

    def load_books(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                books_data = data.get('books', [])
                if not isinstance(books_data, list):
                    books_data = []
                books = [Book(book['title'], book['author'], book['isbn']) for book in books_data]
                return books
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self, books):
        data = {'books': books}
        self._save_data(data)

    def load_users(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                users_data = data.get('users', [])
                if not isinstance(users_data, list):
                    users_data = []
                users = [User(user['name'], user['user_id']) for user in users_data]
                return users
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_users(self, users):
        data = {'users': users}
        self._save_data(data)

    def load_checkouts(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                checkouts_data = data.get('checkouts', [])
                if not isinstance(checkouts_data, list):
                    checkouts_data = []
                return checkouts_data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_checkouts(self, checkouts):
        data = {'checkouts': checkouts}
        self._save_data(data)

    def _save_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, cls=BookEncoder)
