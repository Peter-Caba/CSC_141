class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
       

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

# Creating several instances of User
user1 = User("Deandre", "jones", 18, "deandre.jonesoutlook.com", "Baltimore")
user2 = User("Tyler", "stills", 18, "tyler.stilloutlook.com", "Baltimore")
user3 = User("Peter", "caba", 19, "peter.caba@outlook.com", "Baltimore")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
