### 6-7. People: Start with the program you wrote for
# Exercise 6-1 (page 102). Make two new dictionaries
# representing different people, and store all three
# dictionaries in a list called people. Loop through
# your list of people. As you loop through the list,
# print everything you know about each person.


people = []

person_0 = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': '27',
    'city': 'dallas',
    }
people.append(person_0)

person_1 = {
    'first_name': 'jimmi',
    'last_name': 'hendrix',
    'age': '26',
    'city': 'london',
    }
people.append(person_1)

person_2 = {
    'first_name': 'lemmy',
    'last_name': 'killmister',
    'age': '30',
    'city': 'birmingham',
    }
people.append(person_2)

for name in people:
    full_name = name['first_name'].title() + ' ' + name['last_name'].title()
    age = str(name['age'])
    city = name['city'].title()
    print('\nFull name: ' + full_name)
    print('\tAge: ' + age)
    print('\tFrom: ' + city)
