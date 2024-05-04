class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class UserManager:
    def __init__(self, storage):
        self.storage = storage
        self.users = self.storage.load_users()

    def add_user(self, name, user_id):
        if(self.if_user_exist(user_id=user_id)):
            print("User already exist.")
            return
        new_user = User(name, user_id)
        self.users.append(new_user)
        self.storage.save_users(self.users)
        print("User added.")

    def update_user(self, user_id, name=None):
        is_updated=False
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                self.storage.save_users(self.users)
                is_updated=True
        if(is_updated):
            print("User updated.")
        else:
            print("User does not exist")    
       

    def delete_user(self, user_id):
        prev_count=len(self.users)
        self.users = [user for user in self.users if user.user_id != user_id]
        after_count=len(self.users)
        if(prev_count==after_count):
            print("User does not exist")
        else:
            print("User deleted")
        self.storage.save_users(self.users)

    def list_users(self):
        for user in self.users:
            print(f"Name: {user.name}, User ID: {user.user_id}")

    def search_by_name(self, name):
        found_users = [user for user in self.users if user.name == name]
        if found_users:
            for user in found_users:
                print(f"Name: {user.name}, User ID: {user.user_id}")
        else:
            print("No user found with that name.")

    def search_by_id(self, user_id):
        found_users = [user for user in self.users if user.user_id == user_id]
        if found_users:
            for user in found_users:
                print(f"Name: {user.name}, User ID: {user.user_id}")
        else:
            print("No user found with that ID.")
    
    def if_user_exist(self, user_id):
        found_users = [user for user in self.users if user.user_id == user_id]
        if len(found_users)>0:
            return True
        else:
            return False
            
