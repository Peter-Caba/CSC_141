def make_album(artist, title, num_songs=None):
    album = {
        'artist': artist,
        'title': title,
    }
    if num_songs:
        album['number_of_songs'] = num_songs
    return album

album1 = make_album("The Weeknd", "After Hours", 14)
album2 = make_album("Taylor Swift", "1989")
album3 = make_album("Ed Sheeran", "Divide", 16)


print(album2)
print(album3)

