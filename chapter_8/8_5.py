# 8-5. Cities: Write a function called describe_city() that
# accepts the name of a city and its country. The function
# should print a simple sentence, such as Reykjavik is in Iceland.
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one
# of which is not in the default country.


def describe_city(city_name, country='italy'):
     print(city_name.title() + " is in " + country.title() + ".")

describe_city('roma')
print('---')
describe_city('marina di grosseto')
print('---')
describe_city('kyiv', 'ukraine')
print('---')
describe_city('moscow', 'russia')
print('---')
describe_city('minsk', country='belarus')
