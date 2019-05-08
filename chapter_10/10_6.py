# 10-6. Addition: One common problem when prompting for numerical
# input occurs when people provide text instead of numbers. When
# you try to convert the input to an int, you’ll get a TypeError.
# Write a program that prompts for two numbers. Add them together
# and print the result. Catch the ValueError if either input value
# is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text
# instead of a number.

try:
    a = input("Enter a number: ")
    a = int(a)

    b = input("Enter a number: ")
    b = int(b)

except ValueError:
    print("You need to enter a nuber!")

else:
    print(f"The sum of {str(a)} and {str(b)} is {str(a+b)}")
