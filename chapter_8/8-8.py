# 8-8. User Albums: Start with your program from Exercise 8-7.
# Write a while loop that allows users to enter an album’s
# artist and title. Once you have that information, call
# make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.


def make_album(artist, album):
    album = {'artist': artist.title(), 'album': album.title(),}
    return album

while True:
    print('\nEnter the artist\'s name.')
    print('Enter "q" to quit')
    artist = input('Artist\'s name: ')
    if artist.lower() == 'q':
        break

    print('\nEnter the albums\'s name.')
    print('Enter "q" to quit')
    album = input('Album\'s name: ')
    if album.lower() == 'q':
        break

    formatted = make_album(artist, album)
    print(formatted)
