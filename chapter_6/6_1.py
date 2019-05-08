### 6-1. Person: Use a dictionary to store information
# about a person you know. Store their first name,
# last name, age, and the city in which they live. You
# should have keys such as first_name, last_name,
# age, and city. Print each piece of information stored
# in your dictionary.


friend = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': '27',
    'city': 'dallas',
    }

print('First name: ' + friend['first_name'].title())
print('Last name: ' + friend['last_name'].title())
print('Age: ' + friend['age'])
print('City: ' + friend['city'].title())
