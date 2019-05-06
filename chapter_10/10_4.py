# 10-4. Guest Book: Write a while loop that prompts users for their
# name. When they enter their name, print a greeting to the screen
# and add a line recording their visit in a file called guest_book.txt.
# Make sure each entry appears on a new line in the file.

filename = "guest_book.txt"

while True:
    name = input("What is your name? \n(enter 'q' to quit): ")
    if name == "q":
        break
    else:
        msg = "Hello, " + name.title().strip() + "!"
        msg += " You've been added to the guest book!\n"
        print(msg)

        with open(filename, "a") as file_object:
            file_object.write(msg)
