# 10-13. Verify User: The final listing for remember_me.py assumes
# either that the user has already entered their username or that
# the program is running for the first time. We should modify it
# in case the current user is not the person who last used the
# program. Before printing a welcome back message in greet_user(),
# ask the user if this is the correct username. If it’s not, call
# get_new_username() to get the correct username.

import json

filename = 'username.json'

def get_stored_name():
    """Gets stored name, if exist."""
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError:
        return None
    else:
        return username

def get_new_username():
    """Get new username, if doesn't exist."""
    username = input("What is your name?\n:")
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        return username

def greet_user():
    """Greet the user."""
    username = get_stored_name()
    if username:
        answer = input(f"Are you {username.title()}? (yes/no)\n:")
        if answer.lower() == 'yes':
            print(f"Welcome back, {username.title()}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username.title()}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username.title()}!")

greet_user()
