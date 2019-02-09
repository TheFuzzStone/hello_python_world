### 7-9. No Pastrami: Using the list sandwich_orders
# from Exercise 7-8, make sure the sandwich
# 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print
# a message saying the deli has run out of pastrami,
# and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami
# sandwiches end up in finished_sandwiches.


sandwich_orders = ['bagel toast', 'pastrami', 'carrozza',
    'chili burger', 'deli', 'pastrami', 'vegetarian sandwich', 'elvis',
    'fairy bread', 'gerber', 'jucy lucy', 'mitraillette', 'pastrami',]
finished_sandwiches = []

print('Sorry, we\'re all out of pastrami.\n')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich.title() + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwithces have been made:")
for sandwich in finished_sandwiches:
    print("* " + sandwich.title())
