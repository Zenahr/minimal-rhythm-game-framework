song_1 = "10010010101001001010" # 1 -> drum, 0 -> snare
song_2 = "100100101-10010---" # - -> pause

def play_song(song):
    """This should play basic sounds corresponding to the characters of the string.
    The song will be repeated infinetely. The length of the song is defined by the song itself."""
    for note in song:
        print(note)

play_song(song_1)