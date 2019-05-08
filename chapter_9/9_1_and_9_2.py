# 9-1. Restaurant: Make a class called Restaurant. The __init__() method
# for Restaurant should store two attributes: a restaurant_name and a
# cuisine_type. Make a method called describe_restaurant() that
# prints these two pieces of information, and a method called
# open_restaurant() that prints a message indicating that the
# restaurant is open.Make an instance called restaurant from your
# class. Print the two attributes individually, and then call both
# methods.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title() + ' kitchen.'

    def describe_restaurant(self):
        """Describes the restaurant"""
        print('Restaurants name: ' + self.restaurant_name)
        msg = 'This restaurant specializes in ' + self.cuisine_type
        print(msg)

    def open_restaurant(self):
        """Display the message that the restaurant is open."""
        print("The restaurant is open now. Welcome!\n")

restaurant = Restaurant('chang pang', 'asian')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_1 = Restaurant('la mafia', 'italian')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant('saint patrick', 'irish')
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
