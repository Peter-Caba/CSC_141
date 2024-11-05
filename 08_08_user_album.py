def make_album(artist, title, num_songs=None):
    album = {
        'artist': artist,
        'title': title,
    }
    if num_songs:
        album['number_of_songs'] = num_songs
    return album

while True:
    print("\nEnter album details (or 'q' to quit):")
    
    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break
    
    title = input("Album title: ")
    if title.lower() == 'q':
        break

    num_songs_input = input("Number of songs (press Enter to skip): ")
    num_songs = int(num_songs_input) if num_songs_input else None

    album = make_album(artist, title, num_songs)
    print("\nAlbum created:", album)
