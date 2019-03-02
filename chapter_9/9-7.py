# 9-7. Admin: An administrator is a special kind of user. Write a
# class called Admin that inherits from the User class you wrote
# in Exercise 9-3 (page 166) or Exercise 9-5 (page 171). Add an
# attribute, privileges, that stores a list of strings like
# "can add post", "can delete post" , "can ban user" , and so on.
# Write a method called show_privileges() that lists the
# administrator’s set of privileges. Create an instance of Admin,
# and call your method.


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

class Admin(User):
    """Admin class"""
    def __init__(self, first_name, email, last_name='admin', country='forum',
                 city='', age=''):
        super().__init__(first_name, last_name, country, city, age, email)
        self.privileges = [
        'can add post', 'can delete any post or topic', 'can ban user',
        'can add moderator', 'can change theme']

    def describe_user(self):
        """Describes the admin."""
        print('User: ' + self.first_name)
        print("Email: " + self.email)

    def greet_user(self):
        """Greeting for dear Admin."""
        print('\nWelcome back dear ' + self.first_name.title() + '!')
        print('---------------------------')

    def show_privileges(self):
        print('Admin privileges: ')
        for privilege in self.privileges:
            print('- ' + privilege)
        print('---------------------------')

admin = Admin('admin', 'admin@protonmail.com')
admin.describe_user()
admin.greet_user()
admin.show_privileges()
