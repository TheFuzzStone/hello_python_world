# 9-5. Login Attempts: Add an attribute called login_attempts
# to your User class from Exercise 9-3 (page 166). Write a
# method called increment_ login_attempts() that increments
# the value of login_attempts by 1. Write another method
# called reset_login_attempts() that resets the value
# of login_attempts to 0. Make an instance of the User class
# and call increment_login_attempts() several times. Print the
# value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts().
# Print login_attempts again to make sure it was reset to 0.


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

user_1 = User('lemmy', 'killmister', 'england', 'birmingham', 70,
              'lemmy@motorhead.com')
user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

msg_login = 'Numer of login attempts for '
print(msg_login + user_1.full_name + ": " + str(user_1.login_attempts))
print('---------------------------')

user_1.reset_login_attempts()
msg_reset = 'Number of login attempts for '
print(msg_reset + user_1.full_name + ' reseted to: '
+ str(user_1.login_attempts))
