
from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        self.id = CURSOR.lastrowid  # Assign the last inserted row ID to the instance
        CONN.commit()

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

# Create the songs table if it doesn't exist
Song.create_table()

# Create a new song and print its name and album
song = Song.create("Hello", "25")
print(song.name)
print(song.album)
