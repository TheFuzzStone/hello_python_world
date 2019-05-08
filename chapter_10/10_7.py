# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a
# while loop so the user can continue entering numbers even if they
# make a mistake and enter text instead of a number.

print("(enter 'q' to quit in any moment)")
while True:
    try:
        a = input("Enter a number: ")
        if a == 'q':
            break
        else:
            a = int(a)

        b = input("Enter a number: ")
        if b == 'q':
            break
        b = int(b)

    except ValueError:
        print("You need to enter a nuber!")

    else:
        print(f"The sum of {str(a)} and {str(b)} is {str(a+b)}")
