
class User:
    def __init__(self, username, first_name, last_name):
        """Initialize the user’s attributes."""
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Return a description of the user."""
        return f"Username: {self.username}, Name: {self.first_name} {self.last_name}"
class Privileges:
    def __init__(self):
        """Initialize the list of privileges."""
        self.privileges = [ "can add post", "can delete post", "can ban user", "can edit post" ]
    
    def show_privileges(self):
        """Display the list of privileges."""
        print("The administrator has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, username, first_name, last_name):
        """Initialize attributes of the parent class and add privileges."""
        super().__init__(username, first_name, last_name)
        self.privileges = Privileges()
