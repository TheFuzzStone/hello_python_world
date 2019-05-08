### 6-6. Polling: Use the code in favorite_languages.py (page 104).
# •Make a list of people who should take the favorite languages poll.
# Includesome names that are already in the dictionary and some that are not.
# •Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("--------------------------------------")

others = ['andy', 'john', 'phil', 'george', 'edward',]
for other in others:
    if other in favorite_languages.keys():
        print(other.title() + ", thank's for taking the poll!")
    else:
        print(other.title() + " what's your favorite programming \
language?")
