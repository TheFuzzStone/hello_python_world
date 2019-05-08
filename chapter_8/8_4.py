# 8-4. Large Shirts: Modify the make_shirt() function so
# that shirts are large by default with a message that
#  reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt
#of any size with a different message.

def make_shirt(message="I love Python", size='l'):
    print('\nMaking a T-shirt!...\nYour T-shirt is done!' +
    '\nSize: ' + size.upper() + '\nMessage: \n\t' + message)

make_shirt()
make_shirt(size='s')
make_shirt(message='print("Hello World")', size="XL")
