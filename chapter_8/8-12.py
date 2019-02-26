# 8-12. Sandwiches: Write a function that accepts a list of
# items a person wantson a sandwich. The function should
#  have one parameter that collects as many items as the
# function call provides, and it should print a summary of
# the sandwich that is being ordered. Call the function three
# times, using a different number of arguments each time.

def making_sandwiches(*ingredients):
    print('Making sandwich with following ingredients: ')
    for ingredient in ingredients:
        print('- ' + ingredient)
    print('Enjoy your sandwich! :-)\n')

making_sandwiches('salami')
making_sandwiches('turkey breast', 'bacon', 'grilled cheese')
making_sandwiches('roast beef', 'ham and cheese', 'ketchup', 'relish',
'mustard', 'vegetables',)
