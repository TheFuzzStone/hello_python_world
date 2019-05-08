# 9-8. Privileges: Write a separate Privileges class. The class should
# have one attribute, privileges, that stores a list of strings as
# described in Exercise 9-7. Move the show_privileges() method to
# this class. Make a Privileges instance as an attribute in the Admin
# class. Create a new instance of Admin and use your method to show
# its privileges.


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
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increasing login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resetting login attempts."""
        self.login_attempts = 0

class Privileges():
    """Only for admins privileges list."""
    def __init__(self):
        self.privileges = [
        'can add post', 'can delete post', 'can ban user',
        'can add moderator', 'can change theme', 'can close topics']

    def show_privileges(self):
        print('Your privileges: ')
        for privilege in self.privileges:
            print('- ' + privilege)

class Admin(User):
    """Admin class"""
    def __init__(self, first_name, email, last_name='admin', country='forum',
                 city='', age=''):
        super().__init__(first_name, last_name, country, city, age, email)
        self.privileges = Privileges()

    def describe_user(self):
        """Describes the admin."""
        print('User: ' + self.first_name)
        print("Email: " + self.email)

    def greet_user(self):
        """Greeting for dear Admin."""
        print('\nWelcome back dear ' + self.first_name.title() + '!')
        print('---------------------------')

admin = Admin('admin', 'admin@protonmail.com')
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()

# one more calling the admin
