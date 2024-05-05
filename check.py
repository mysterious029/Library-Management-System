import os
from user import UserManager
from storage import JSONStorage
class CheckInOut:
    def __init__(self, storage):
        self.storage = storage
        self.checkouts = self.storage.load_checkouts()
        self.user_manager=UserManager(JSONStorage(os.path.join('data', "users.json")))

    def check_out(self, user_id, isbn):
        if(self.user_manager.if_user_exist(user_id=user_id)):
            self.checkouts.append((user_id, isbn))
            self.storage.save_checkouts(self.checkouts)
            print("Book checked out.")
        else:
            print("user does not exist.")

    def check_in(self, user_id, isbn):
        prev_count=len(self.checkouts)
        self.checkouts = [(uid, book) for uid, book in self.checkouts if uid != user_id or book != isbn]
        after_count=len(self.checkouts)
        if(prev_count==after_count):
            print("book not checked in")
        else:
            print("Book checked in.")
        self.storage.save_checkouts(self.checkouts)

    def get_checked_out_books(self):
        return self.checkouts

    def is_book_checked_out(self, isbn):
        return any(book == isbn for _, book in self.checkouts)
    