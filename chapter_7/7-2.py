### 7-2. Restaurant Seating: Write a program that asks the user
# how many people are in their dinner group. If the answer
# is more than eight, print a message saying they’ll have to
# wait for a table. Otherwise, report that their table is ready.

q = input('How many guests will be with you tonight at our restaurant?: ')
q = int(q)
if q > 8:
    print('We\'re sorry, but we\'re not gonna have so many available \
seats at the moment.')
else:
    print('Your booking for ' +  str(q) + ' people is confirmed. \
Have a good time!')
