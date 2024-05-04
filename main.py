import book
import user
import check
import storage
import os

def main_menu():
    print("\nLibrary Management System")
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Check Out/In Book")
    print("4. Exit")
    choice = input("Enter choice: ")
    return choice

def manage_books(book_manager):
    while True:
        print("\nBook Management")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. List Books")
        print("5. Search by Title")
        print("6. Search by Author")
        print("7. Search by ISBN")
        print("8. Back to Main Menu")
        choice = input("Enter choice: ")
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_manager.add_book(title, author, isbn)
            print("Book added.")
        elif choice == '2':
            isbn = input("Enter ISBN of the book to update: ")
            new_title = input("Enter new title (press Enter to skip): ")
            new_author = input("Enter new author (press Enter to skip): ")
            if new_title or new_author:
                book_manager.update_book(isbn, new_title, new_author)
                
            else:
                print("No changes made.")
        elif choice == '3':
            isbn = input("Enter ISBN of the book to delete: ")
            book_manager.delete_book(isbn)
            
        elif choice == '4':
            book_manager.list_books()
        elif choice == '5':
            title = input("Enter title to search: ")
            book_manager.search_by_title(title)
        elif choice == '6':
            author = input("Enter author to search: ")
            book_manager.search_by_author(author)
        elif choice == '7':
            isbn = input("Enter ISBN to search: ")
            book_manager.search_by_isbn(isbn)
        elif choice == '8':
            break
        else:
            print("Invalid choice, please try again.")

def manage_users(user_manager):
    while True:
        print("\nUser Management")
        print("1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. List Users")
        print("5. Search by Name")
        print("6. Search by ID")
        print("7. Back to Main Menu")
        choice = input("Enter choice: ")
        if choice == '1':
            name = input("Enter name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(name, user_id)
            
        elif choice == '2':
            user_id = input("Enter user ID of the user to update: ")
            new_name = input("Enter new name (press Enter to skip): ")
            if new_name:
                user_manager.update_user(user_id, new_name)
              
            else:
                print("No changes made.")
        elif choice == '3':
            user_id = input("Enter user ID of the user to delete: ")
            user_manager.delete_user(user_id)
        elif choice == '4':
            user_manager.list_users()
        elif choice == '5':
            name = input("Enter name to search: ")
            user_manager.search_by_name(name)
        elif choice == '6':
            user_id = input("Enter ID to search: ")
            user_manager.search_by_id(user_id)
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")

def manage_checkout(check_manager):
    while True:
        print("\nCheck In/Out Management")
        print("1. Check Out Book")
        print("2. Check In Book")
        print("3. View Checked Out Books")
        # print("4. View Checked In Books")
        print("4. Back to Main Menu")
        choice = input("Enter choice: ")
        if choice == '1':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to check out: ")
            check_manager.check_out(user_id, isbn)
            
        elif choice == '2':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to check in: ")
            check_manager.check_in(user_id, isbn)
            
        elif choice == '3':
            print("Checked Out Books:")
            for checkout in check_manager.get_checked_out_books():
                print(f"User ID: {checkout[0]}, ISBN: {checkout[1]}")
        # elif choice == '4':
        #     print("Checked In Books:")
        #     for checkout in check_manager.get_checked_in_books():
        #         print(f"User ID: {checkout[0]}, ISBN: {checkout[1]}")        
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def main():
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    book_storage = storage.JSONStorage(os.path.join(data_dir, "books.json"))
    user_storage = storage.JSONStorage(os.path.join(data_dir, "users.json"))
    check_storage = storage.JSONStorage(os.path.join(data_dir, "checkouts.json"))
    # check_storage_in = storage.JSONStorage(os.path.join(data_dir, "checkins.json"))

    book_manager = book.BookManager(book_storage)
    user_manager = user.UserManager(user_storage)
    check_manager = check.CheckInOut(check_storage)
    
    while True:
        choice = main_menu()
        if choice == '1':
            manage_books(book_manager)
        elif choice == '2':
            manage_users(user_manager)
        elif choice == '3':
            manage_checkout(check_manager)
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
