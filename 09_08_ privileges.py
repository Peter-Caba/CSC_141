
class Privileges:
    def __init__(self):

        self.privileges = [ "can add post", "can delete post",  "can ban user",   "can edit post" ]
    
    def show_privileges(self):
        print("The administrator has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class User:
    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        return f"Username: {self.username}, Name: {self.first_name} {self.last_name}"


class Admin(User):
    def __init__(self, username, first_name, last_name):
        super().__init__(username, first_name, last_name)
      
        self.privileges = Privileges()

admin_user = Admin('admin01', 'Alice', 'Smith')


admin_user.privileges.show_privileges()
