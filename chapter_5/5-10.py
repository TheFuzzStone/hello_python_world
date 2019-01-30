### 5-10. Checking Usernames: Do the following to create
# a program that simulates how websites ensure that
# everyone has a unique username.
# •Make a list of five or more usernames called current_users.
# •Make another list of five usernames called new_users. Make
# sure one or two of the new usernames are also in the current_users list.
# •Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# •Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted.

current_users = ['Alice', 'BoB', 'CARoL', 'DAVE', 'eARL', 'FraNK', 'John']
new_users = ['George', 'Janis', 'dave', 'Peter', 'CARL', 'JOHN']

comparsion_case_sensitive_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in comparsion_case_sensitive_lower:
        print('Sorry, but nickname: ' + new_user + ' is already taken. Please, choose a different nickname.')
    else:
        print('Nickname: ' + new_user + ' seems available for registration.')
