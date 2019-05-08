### 6-10. Favorite Numbers: Modify your program from
# Exercise 6-2 (page 102) so each person can have more
# than one favorite number. Then print each person’s
# name along with their favorite numbers.


names_and_numbers = {
    'alice': [8, 22, 43, 24,],
    'bob': [2, 13, 46, 77,],
    'carl': [3, 11,],
    'dave': [4, 59, 1,],
    'earl': [8,],
    }

for name, numbers in names_and_numbers.items():
    if len(numbers) < 2:
        print("\n" + name.title() + "'s favorite number is:")
        for number in numbers:
            print(str(number))
    else:
        print("\n" + name.title() + "'s favorite numbers are:")
        for number in numbers:
            print(str(number))
