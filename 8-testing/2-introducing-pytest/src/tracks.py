import pdb
def clean_track(track):
    return track.split(' - ')[0]

def find_song(songs, name):
    found_song = [song for song in songs if song['song'] == name]
    next(iter(found_song), None)

def sort_songs(songs):
    return sorted(songs, key=lambda element: element['song'])
