# 7-10. Dream Vacation: Write a program that polls users
# about their dream vacation. Write a prompt similar
# to If you could visit one place in the world,
# where would you go? Include a block of code that
# prints the results of the poll.

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?\n")
    response = input("\nIn which country would you like to spend your vacation?\n")
    responses[name] = response
    repeat = input('Would you like to let another person respond? \
(yes / no): ')
    if repeat.lower() == 'no':
        polling_active = False

for name, response in responses.items():
    print("-----------------------------------------")
    print("\n" + name.title() + " would like to spend vacation in " +
    response.title() + ".")
