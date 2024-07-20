class Song:

    count = 0
    genres = []
    artists = []
    genre_count= {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        

    @classmethod                       #increments the value of count by one
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):      # adds any new genres to a class attribute genres
        if not genre in cls.genres:
            cls.genres.append(genre)
        
    @classmethod
    def add_to_artists(cls, artist):     #adds any new artists to a class attribute artists
        if not artist in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1


    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1























ninety_nine_problems = Song("99 Problems", "Jay-z", "Rap")

print(ninety_nine_problems.name)
print(ninety_nine_problems.artist)
print(ninety_nine_problems.genre)

print(Song.artist_count)