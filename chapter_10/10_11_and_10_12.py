# 10-12. Favorite Number Remembered: Combine the two programs from
# Exercise 10-11 into one file. If the number is already stored,
# report the favorite number to the user. If not, prompt for the
# user’s favorite number and store it in a file. Run the program
# twice to see that it works.

import json
filename = 'favorite_number.json'

try:
    with open(filename) as file_object:
        favorite_number = json.load(file_object)

except FileNotFoundError:
    favorite_number = 'favorite_number.json'
    number = input("Enter your favorite number: ")
    print(f"I will remember it!")

    with open(favorite_number, 'w') as file_object:
        json.dump(number, file_object)
else:
    print(f"I know your favorite number: {favorite_number}")
