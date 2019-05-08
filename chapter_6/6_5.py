### 6-5. Rivers: Make a dictionary containing three major rivers
# and the country each river runs through. One key-value pair
# might be 'nile': 'egypt'.
# •Use a loop to print a sentence about each river, such as
# The Nile runs through Egypt.
# •Use a loop to print the name of each river included in the
# dictionary.
# •Use a loop to print the name of each country included in
# the dictionary.

rivers_countries = {
    'elbe': 'czech republic',
    'po': 'italy',
    'rhine': 'france',
    'tagus': 'spain',
    'gudena': 'denmark'
    }

for r, c in rivers_countries.items():
    print("The " + r.title() + " runs through " +
    c.title() + ".")

print("\nThe following rivers are included in this dictionary:")
for r in rivers_countries:
    print('- ' + r.title())

print("\nThe following countries are included in this dictionary:")
for c in rivers_countries.values():
    print("- " + c.title())
