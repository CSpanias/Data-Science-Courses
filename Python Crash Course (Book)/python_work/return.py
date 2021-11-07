# 8.6
def city_country(city_name, country):
    print(f'{city_name.title()}, {country.title()}')

city_country('athens', 'greece')
city_country('edinburgh', 'scotland')
city_country('london', 'england')

# 8.7
def make_album(artist_name, album_title, number_of_songs=None):
    music_album = {
            'artist_name': artist_name,
            'album_title': album_title,
    }

    if number_of_songs:
        music_album['songs_number'] = number_of_songs

    return music_album

album_1 = make_album('active member', 'lalala')
print(album_1)
album_2 = make_album('active member', 'lilili')
print(album_2)
album_3 = make_album('active member', 'lololo')
print(album_3)
album_4 = make_album('txc', 'polis_ealo', 12)
print(album_4)

# 8.8
while True:
    album_title = input('Enter the title of the album: ')
    print('enter "q" to quit at any time')
    if album_title == 'q':
        break

    artist_name = input('Enter the title of the artist: ')
    print('enter "q" to quit at any time')
    if artist_name == 'q':
        break

    album_1 = make_album(artist_name, album_title)
    print(album_1)