# 8-6. City Names: Write a function called city_country()
# that takes in the name of a city and its country.
# The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs,
# and print the value that’s returned.

def city_country(city, country):
    city_and_country = city + ', ' + country
    return city_and_country.title()

c_plus_c = city_country('rome', 'italy')
print(c_plus_c)

c_plus_c = city_country('paris', 'france')
print(c_plus_c)

c_plus_c = city_country('prague', 'czech repuplic')
print(c_plus_c)
