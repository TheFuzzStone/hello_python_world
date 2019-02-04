### 6-9. Favorite Places: Make a dictionary called favorite_places.
# Think of three names to use as keys in the dictionary, and store
# one to three favorite places for each person. To make this
# exercise a bit more interesting, ask some friends to name a few
# of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.

favorite_places = {
    'alice': ['london', 'paris'],
    'bob': ['new orleans'],
    'carol': ['minsk', 'kiev', 'moscow'],
    'dave': ['prague', 'rome', 'madrid', 'lisabon']
    }

for name, places in favorite_places.items():
    if len(places) < 2:
        print("\n" + name.title() + "'s favorite place is: ")
        for place in places:
            print("\t* " + place.title())
    else:
        print("\n" + name.title() + "'s favorite places are: ")
        for place in places:
            print("\t* " + place.title())
