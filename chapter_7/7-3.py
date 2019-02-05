### 7-3. Multiples of Ten: Ask the user for a number, and then
# report whether the number is a multiple of 10 or not.



n = input("Give me a number, please: ")
n = int(n)

if n % 10 == 0:
    print(str(n) + " is a multiple of 10.")
else:
    print("Sorry, but " + str(n) + " is not a multiple of 10.")
