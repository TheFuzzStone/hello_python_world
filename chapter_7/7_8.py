### 7-8. Deli: Make a list called sandwich_orders and fill
# it with the names of vari-ous sandwiches. Then make an
# empty list called finished_sandwiches. Loop through the
# list of sandwich orders and print a message for each order,
# such as I made your tuna sandwich. As each sandwich is made,
# move it to the list of finished sandwiches. After all the
# sandwiches have been made, print a message listing each
# sandwich that was made.


sandwich_orders = ['bagel toast', 'carrozza',
    'chili burger', 'deli', 'vegetarian sandwich', 'elvis',
    'fairy bread', 'gerber', 'jucy lucy', 'mitraillette',]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich.title() + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwithces have been made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
