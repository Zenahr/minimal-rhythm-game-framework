import pyglet

""" load assets in memory once on start"""
base_sound = pyglet.resource.media('assets/sounds/base.wav', streaming=False)
snare_sound = pyglet.resource.media('assets/sounds/snare.wav', streaming=False)

song_1 = "10010010101001001010" # 1 -> drum, 0 -> snare
song_2 = "100100101-10010---" # - -> pause

def play_song(song):
    """This should play basic sounds corresponding to the characters of the string.
    The song will be repeated infinetely. The length of the song is defined by the song itself."""
    for note in song:
        if(note == "1"):
            play("base-drum")
        if(note == "0"):
            play("snare-drum")
        if(note == "-"):
            play("nothing")

def play(instrument):
    if(instrument == "base-drum"):
        # print("base-drum") # DEBUG
        base_sound.play()
    elif(instrument == "snare-drum"):
        # print("snare-drum") # DEBUG
        snare_sound.play()
    elif(instrument == "nothing"):
        # print("nothing") # DEBUG
        pass

# play_song(song_1)
snare_sound.play()
