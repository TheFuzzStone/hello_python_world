# 9-10. Imported Restaurant: Using your latest Restaurant class, store
# it in a module. Make a separate file that imports Restaurant.
# Make a Restaurant instance, and call one of Restaurant’s methods to
# show that the import statement is working properly.

from restaurant import Restaurant

restaurant_1 = Restaurant('la mafia', 'italian')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
