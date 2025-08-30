# logic.py

from abc import ABC, abstractmethod
from data import predefined_songs, predefined_users, predefined_playlists

class User(ABC):
    total_users = 0

    def __init__(self, username, email, subscription_type="Free"):
        self.username = username
        self._subscription_type = subscription_type
        if "@" in email and "." in email:
            self.__email = email
        else:
            raise ValueError("❌ Invalid email address.")
        User.total_users += 1

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self.__email = new_email
        else:
            print("❌ Invalid email.")

    @abstractmethod
    def view_profile(self):
        pass

class Listener(User):
    def __init__(self, username, email, subscription_type="Free"):
        super().__init__(username, email, subscription_type)
        self.playlists = []

    def view_profile(self):
        print(f"Listener: {self.username}, Sub: {self._subscription_type}, Email: {self.get_email()}")

class Song:
    total_songs = 0

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self._duration = duration
        self.__play_count = 0
        Song.total_songs += 1

    def play_song(self):
        self.__play_count += 1
        print(f"▶ Playing '{self.title}' by {self.artist} (Plays: {self.__play_count})")

    def get_play_count(self):
        return self.__play_count

    def display_info(self):
        print(f"{self.title} - {self.artist} ({self._duration}) | Plays: {self.__play_count}")

class Playlist:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.songs = []

    def add_song(self, song, show_message=True):
        self.songs.append(song)
        if show_message:
            print(f"✅ '{song.title}' added to '{self.name}'")

    def display_playlist(self):
        print(f"\n🎶 Playlist: {self.name} (Owner: {self.owner.username})")
        if not self.songs:
            print("No songs yet.")
        else:
            for idx, s in enumerate(self.songs, start=1):
                print(f"{idx}. {s.title} - {s.artist} ({s._duration})")

class Spotify:
    premium_fee = 10

    def __init__(self, name="Spotify"):
        self.name = name
        self.users = []
        self.songs = []
        self.playlists = []

        # Load predefined songs
        for song_dict in predefined_songs:
            self.songs.append(Song(song_dict['title'], song_dict['artist'], song_dict['duration']))

        # Load predefined listeners
        for u in predefined_users:
            try:
                if u["type"] == "Listener":
                    self.users.append(Listener(u["username"], u["email"], u["subscription"]))
            except ValueError:
                pass

        # Load predefined playlists without print messages
        for pl_data in predefined_playlists:
            owner = next((u for u in self.users if isinstance(u, Listener) and u.username == pl_data["owner"]), None)
            if owner:
                pl = Playlist(pl_data["name"], owner)
                for song_title in pl_data["songs"]:
                    song = next((s for s in self.songs if s.title == song_title), None)
                    if song:
                        pl.add_song(song, show_message=False)
                self.playlists.append(pl)
                owner.playlists.append(pl)

    def register_listener(self, username, email, sub="Free"):
        listener = Listener(username, email, sub)
        self.users.append(listener)
        print(f"👤 Registered {username} as Listener")
        return listener

    def add_song(self, title, artist_name, duration):
        song = Song(title, artist_name, duration)
        self.songs.append(song)
        print(f"🎵 New song: '{title}' by {artist_name}")

    def show_all_users(self):
        print("\n--- All Users ---")
        for u in self.users:
            u.view_profile()

    def show_user_playlists(self, username):
        listener = next((u for u in self.users if isinstance(u, Listener) and u.username == username), None)
        if not listener:
            print("⚠️ Listener not found")
        else:
            for pl in listener.playlists:
                pl.display_playlist()

    def show_all_songs(self):
        print("\n--- All Songs ---")
        for idx, song in enumerate(self.songs, start=1):
            print(f"{idx}. ", end='')
            song.display_info()

    def play_song(self, index):
        if 0 <= index < len(self.songs):
            self.songs[index].play_song()
        else:
            print("Invalid song number")

    def system_report(self):
        print("\n=== Spotify Report ===")
        print(f"Total Users: {len(self.users)}")
        print(f"Total Songs: {len(self.songs)}")
        print(f"Total Playlists: {len(self.playlists)}")
        print(f"Total Revenue: ${Spotify.calculate_revenue(self.users)}")

    @staticmethod
    def calculate_revenue(users):
        revenue = 0
        for u in users:
            if isinstance(u, Listener) and u._subscription_type.lower() == "premium":
                revenue += Spotify.premium_fee
        return revenue
