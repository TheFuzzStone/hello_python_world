# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of
# restaurant. Write a class called IceCreamStand that inherits
# from the Restaurant class you wrote in Exercise 9-1 (page 166)
# or Exercise 9-4 (page 171). Either version of the class will
# work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method
# that displays these flavors. Create an instance of IceCreamStand,
# and call this method.


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        if cuisine_type == 'desserts':
            self.cuisine_type = cuisine_type + '.'
        else:
            self.cuisine_type = cuisine_type.title() + ' kitchen.'

    def describe_restaurant(self):
        """Describes the restaurant"""
        print('Restaurants name: ' + self.restaurant_name)
        msg = 'This restaurant specializes in ' + self.cuisine_type
        print(msg)

    def open_restaurant(self):
        """Display the message that the restaurant is open."""
        print("The restaurant is open now. Welcome!\n")


class IceCreamStand(Restaurant):
    """Ice cream stand"""
    def __init__(self, restaurant_name, cuisine_type='desserts'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['sesame', 'banana nut', 'bubblegum',
        'coffee and cookie', 'oak tree']

    def ice_cream_list(self):
        """Display ice cream flavors."""
        msg = 'Available ice cream flavor list:'
        print(msg)
        for flavor in self.flavors:
            print('- ' + flavor.title())

ice_cream_land = IceCreamStand('ice cream land')
ice_cream_land.describe_restaurant()
ice_cream_land.ice_cream_list()
