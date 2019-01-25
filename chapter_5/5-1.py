#5-1. Conditional Tests: Write a series of conditional tests.
#Print a statement #describing each test and your prediction for
# the results of each test. Your code
#should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')

#Look closely at your results, and make sure you understand why each line
#evaluates to True or False.

cars = ['buick', 'pontiac', 'subaru', 'toyota', 'saab', 'audi', 'bmw']
car = cars.pop(-2)
if car == 'audi':
    print('This is ' + car.title() + '. The statement is \'True\':')
else:
    print('<<<It\'s not Audi. Statement is \'False\'>>>')
print(car == 'audi')
print('----------------------------------------')


print('Is car == bmw? Will be False, because I\'ve popped "Audi"\
 in previous step:')
print(car == 'bmw')
print('----------------------------------------')


print('Is audi == Audi? Nope, because testing for equality is case sensitive \
in Python. So it\'s \'False\':')
print(car.upper() == car)
print('----------------------------------------')


print('Let\'s try \'!=\'. Is car != cars? I think it\'s True:')
print(cars != car)
print('----------------------------------------')


print('Let\'s check \'Ferrari\' in cars. Will be False:')
print('ferrari' in cars)
print('----------------------------------------')


print('Now we\'ll check same \'Ferrari\' using the keyword "not". Will be True,\
 because Ferrari isn\'t in list right now:')
print('ferrari' not in cars)
print('----------------------------------------')


num_0 = 100
num_1 = 99
print("Is (100 > 99) and (99 > 100)? One of the result's is wrong, so \
the whole statement will be \'False\':")
print( (num_0 > num_1) and (num_1 > num_0) )
print('----------------------------------------')


print("Is (100 > 99) or (99 > 100)? The first result is True, so the \
whole statement will be \'True\':")
print( (num_1 < num_0) or (num_0 > num_1) )
print('----------------------------------------')

### I understand why some lines evaluates to True and False.
