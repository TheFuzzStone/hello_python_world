# 9-3. Users: Make a class called User. Create two attributes called
# first_name and last_name, and then create several other attributes
# that are typically stored in a user profile. Make a method called
# describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a personalized
# greeting to the user. Create several instances representing different
# users, and call both methods for each user.

class User():
    """Making the user profile."""
    def __init__(self, first_name, last_name, country, city, age, email):
        """Initizlize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = first_name.title() + ' ' + last_name.title()
        self.country = country.title()
        self.city = city.title()
        self.age = str(age)
        self.email = email

    def describe_user(self):
        """Describes the user"""
        print('User: ' + self.first_name + ' ' + self.last_name)
        print('Location: ' + self.country + ', ' + self.city)
        print('Age: ' + self.age)
        print("Email: " + self.email)

    def greet_user(self):
        """Display greeting message."""
        print('\nWelcome back, ' + self.full_name + '!')
        print('---------------------------')

user_1 = User('john', 'doe', 'czech republic',
              'prague', 23, 'johndoe@protonmail.com')
user_1.describe_user()
user_1.greet_user()

user_2 = User('lemmy', 'killmister', 'england', 'birmingham', 70, '<none>')
user_2.describe_user()
user_2.greet_user()
