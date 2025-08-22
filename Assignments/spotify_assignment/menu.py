# menu.py

from logic import Spotify, Playlist

def run_spotify_cli():
    spotify = Spotify()
    while True:
        print("\n==== Spotify Menu ====")
        print("1. Register Listener")
        print("2. Show All Users")
        print("3. Show All Songs")
        print("4. Play Song")
        print("5. Create Playlist & Add Songs")
        print("6. Show Playlists for Listener")
        print("7. System Report")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter username: ")
            email = input("Enter email: ")
            if "@" not in email or "." not in email:
                print("❌ Invalid email.")
                continue
            sub = input("Subscription (Free/Premium): ").capitalize()
            if sub not in ("Free", "Premium"):
                print("⚠️ Invalid subscription type. Registration cancelled.")
                continue
            try:
                spotify.register_listener(name, email, sub)
            except ValueError as ve:
                print(ve)
                continue

        elif choice == "2":
            spotify.show_all_users()

        elif choice == "3":
            spotify.show_all_songs()

        elif choice == "4":
            spotify.show_all_songs()
            try:
                idx = int(input("Enter song number to play: ")) - 1
                spotify.play_song(idx)
            except:
                print("Invalid input.")

        elif choice == "5":
            username = input("Enter listener username: ")
            listener = next((u for u in spotify.users if u.username == username), None)
            if not listener:
                print("❌ Listener not found")
                continue
            pname = input("Enter playlist name: ")
            pl = Playlist(pname, listener)
            spotify.playlists.append(pl)
            listener.playlists.append(pl)
            spotify.show_all_songs()
            indexes = input("Enter song numbers (comma-separated): ")
            for i in indexes.split(","):
                try:
                    idx = int(i.strip()) - 1
                    if 0 <= idx < len(spotify.songs):
                        pl.add_song(spotify.songs[idx])
                    else:
                        print(f"Song index {idx+1} is out of range.")
                except:
                    print("Invalid song number input.")

        elif choice == "6":
            name = input("Enter listener username: ")
            spotify.show_user_playlists(name)

        elif choice == "7":
            spotify.system_report()

        elif choice == "8":
            print("👋 Exiting...")
            break

        else:
            print("⚠️ Invalid choice")

if __name__ == '__main__':
    run_spotify_cli()
# menu.py

from logic import Spotify, Playlist

def run_spotify_cli():
    spotify = Spotify()
    while True:
        print("\n==== Spotify Menu ====")
        print("1. Register Listener")
        print("2. Show All Users")
        print("3. Show All Songs")
        print("4. Play Song")
        print("5. Create Playlist & Add Songs")
        print("6. Show Playlists for Listener")
        print("7. System Report")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter username: ")
            email = input("Enter email: ")
            if "@" not in email or "." not in email:
                print("❌ Invalid email.")
                continue
            sub = input("Subscription (Free/Premium): ").capitalize()
            if sub not in ("Free", "Premium"):
                print("⚠️ Invalid subscription type. Registration cancelled.")
                continue
            try:
                spotify.register_listener(name, email, sub)
            except ValueError as ve:
                print(ve)
                continue

        elif choice == "2":
            spotify.show_all_users()

        elif choice == "3":
            spotify.show_all_songs()

        elif choice == "4":
            spotify.show_all_songs()
            try:
                idx = int(input("Enter song number to play: ")) - 1
                spotify.play_song(idx)
            except:
                print("Invalid input.")

        elif choice == "5":
            username = input("Enter listener username: ")
            listener = next((u for u in spotify.users if u.username == username), None)
            if not listener:
                print("❌ Listener not found")
                continue
            pname = input("Enter playlist name: ")
            pl = Playlist(pname, listener)
            spotify.playlists.append(pl)
            listener.playlists.append(pl)
            spotify.show_all_songs()
            indexes = input("Enter song numbers (comma-separated): ")
            for i in indexes.split(","):
                try:
                    idx = int(i.strip()) - 1
                    if 0 <= idx < len(spotify.songs):
                        pl.add_song(spotify.songs[idx])
                    else:
                        print(f"Song index {idx+1} is out of range.")
                except:
                    print("Invalid song number input.")

        elif choice == "6":
            name = input("Enter listener username: ")
            spotify.show_user_playlists(name)

        elif choice == "7":
            spotify.system_report()

        elif choice == "8":
            print("👋 Exiting...")
            break

        else:
            print("⚠️ Invalid choice")

if __name__ == '__main__':
    run_spotify_cli()
