# 9-4. Number Served: Start with your program from Exercise 9-1
# (page 166). Add an attribute called number_served with a
# default value of 0. Create an instance called restaurant
# from this class. Print the number of customers the
# restaurant has served, and then change this value and print
# it again. Add a method called set_number_served() that lets
# you set the number of customers that have been served. Call
# this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you
# increment the number of customers who’ve been served. Call
# this method with any num- ber you like that could represent
# how many customers were served in, say, a day of business.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title() + ' kitchen.'
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurant"""
        print('Restaurants name: ' + self.restaurant_name)
        msg = 'This restaurant specializes in ' + self.cuisine_type
        print(msg)

    def open_restaurant(self):
        """Display the message that the restaurant is open."""
        msg_1 = 'The restaurant is open now. Welcome!'
        print(msg_1)

    def set_number_served(self, number):
        """Set the number of visitors served"""
        self.number_served = number

    def  increment_number_served(self, add_additional_number):
        """Increases the number of customers served."""
        self.number_served += add_additional_number

    def display_number_served(self):
        """Display the message of total served customers."""
        print('This restaurant served ' + str(self.number_served) +
        ' customers.')

restaurant = Restaurant('chang pang', 'asian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(142)
restaurant.display_number_served()
restaurant.increment_number_served(1)
restaurant.display_number_served()
restaurant.increment_number_served(1)
restaurant.display_number_served()
print('------------------')

restaurant_1 = Restaurant('la mafia', 'italian')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_1.set_number_served(253)
restaurant_1.display_number_served()
restaurant_1.increment_number_served(14)
restaurant_1.display_number_served()
restaurant_1.increment_number_served(24)
restaurant_1.display_number_served()
print('------------------')
