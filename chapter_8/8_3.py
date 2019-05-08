# 8-3. T-Shirt: Write a function called make_shirt() that
# accepts a size and the text of a message that
# should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the
# message printed on it. Call the function once using
# positional arguments to make a shirt. Call the function
# a second time using keyword arguments.

def make_shirt(size, message):
    print('\nMaking a T-shirt!...\nYour T-shirt is done!' +
    '\nSize: ' + size.upper() + '\nMessage: \n\t' + message)

size = input('What size of T-shirt do you want to buy?: ')
message = input('Enter the message that will be printed on the T-shirt: \n')

make_shirt(size, message)
print('---------------------------------------------------------------')
make_shirt(message=message, size=size)
