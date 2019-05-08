### 6-11. Cities: Make a dictionary called cities. Use the names
# of three cities as keys in your dictionary. Create a dictionary
# of information about each city and include the country that
# the city is in, its approximate population, and one fact about
# that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and
# all of the information you have stored about it.


cities = {
    'rome': {
        'country': 'italy',
        'population': '~4,355,725',
        'fact': 'Rome is the capital city and a special \
comune of Italy (named Comune di Roma Capitale).\
 Rome also serves as the capital of the Lazio region.\
 It is the fourth-most populous city in the European Union by \
population within city limits.',
        },
    'prague': {
        'country': 'czech republic',
        'population': '~1,301,132',
        'fact': 'Prague is the capital and largest city in the\
 Czech Republic, the 14th largest city in the European Union and\
 the historical capital of Bohemia. Situated in the north-west of\
 the country on the Vltava river.',
        },
    'oslo': {
        'country': 'norway',
        'population': '~673,469',
        'fact': 'Oslo is the economic and governmental centre\
 of Norway. The city is also a hub of Norwegian trade, banking, industry\
 and shipping. It is an important centre for maritime industries and maritime\
 trade in Europe. The city is home to many companies within the maritime\
 sector, some of which are among the world\'s largest shipping companies,\
 shipbrokers and maritime insurance brokers. Oslo is a pilot city of the\
 Council of Europe and the European Commission intercultural cities\
 programme.',
        }
}

for city, info_about_cities in cities.items():
    print('\n*City*: ' + city.title())
    print('*Country*: ' + info_about_cities['country'].title())
    print('*Population*: ' + info_about_cities['population'])
    print('*Fact*: \n\t' + info_about_cities['fact'])
    print('----------------------------------------------------------------')
