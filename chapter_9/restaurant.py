class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        if cuisine_type == 'desserts':
            self.cuisine_type = cuisine_type + '.'
        else:
            self.cuisine_type = cuisine_type.title() + ' kitchen.'

    def describe_restaurant(self):
        """Describes the restaurant."""
        print('Restaurants name: ' + self.restaurant_name)
        msg = 'This restaurant specializes in ' + self.cuisine_type
        print(msg)

    def open_restaurant(self):
        """Display the message that the restaurant is open."""
        print("The restaurant is open now. Welcome!\n")
