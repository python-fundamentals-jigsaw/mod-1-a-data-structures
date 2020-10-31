from src.tracks import clean_track, find_song, sort_songs
def test_clean_track():
    track_name = "When I'm Sixty-Four - Remix"
    assert clean_track(track_name) == "When I'm Sixty-Four"

songs = [{'rank': 1, 'song': 'Like a Rolling Stone', 'artist': 'Bob Dylan', 'year': 1965},  
        {'rank': 2, 'song': 'Satisfaction', 'artist': 'The Rolling Stones', 'year': 1965},
        {'rank': 5, 'song': 'Respect', 'artist': 'Aretha Franklin', 'year': 1967}]


def test_find_song_returns_song_dict():
    found_song = find_song(songs, 'Like a Rolling Stone')
    assert found_song == {'rank': 1, 'song': 'Like a Rolling Stone', 'artist': 'Bob Dylan', 'year': 1965}, 'returns song dictionary'
    
def test_find_song_returns_none_if_no_song_found():
    found_song = find_song(songs, 'Like Some Rolling Stone')
    assert found_song == None, 'returns None'

def test_sort_songs():
    assert sort_songs(songs) == [{'rank': 1, 'song': 'Like a Rolling Stone', 'artist': 'Bob Dylan', 'year': 1965}, 
            {'rank': 5, 'song': 'Respect', 'artist': 'Aretha Franklin', 'year': 1967},
            {'rank': 2, 'song': 'Satisfaction', 'artist': 'The Rolling Stones', 'year': 1965}]
    
def test_sort_songs_returns_a_list():
    assert type(sort_songs(songs)) == list
