# data.py

# Predefined song list (10 songs)
predefined_songs = [
    {"title": "Dream On",     "artist": "Rockstar", "duration": "4:30"},
    {"title": "Sky High",     "artist": "DJ Beats", "duration": "3:45"},
    {"title": "Night Road",   "artist": "Blues Man", "duration": "4:02"},
    {"title": "Heartbeat",    "artist": "Mellow", "duration": "3:50"},
    {"title": "Eclipse",      "artist": "SynthWave", "duration": "5:10"},
    {"title": "River",        "artist": "AcousticOne", "duration": "3:58"},
    {"title": "Thunder",      "artist": "PowerPop", "duration": "4:20"},
    {"title": "Light Up",     "artist": "Vox", "duration": "3:32"},
    {"title": "Shadows",      "artist": "IndieSoul", "duration": "4:05"},
    {"title": "Golden Days",  "artist": "RetroBand", "duration": "4:42"}
]

# Predefined users (10 Listeners)
predefined_users = [
    {"username": "alice",  "email": "alice@example.com",  "type": "Listener", "subscription": "Premium"},
    {"username": "bob",    "email": "bob@example.com",    "type": "Listener", "subscription": "Free"},
    {"username": "carol",  "email": "carol@example.com",  "type": "Listener", "subscription": "Premium"},
    {"username": "dave",   "email": "dave@example.com",   "type": "Listener", "subscription": "Free"},
    {"username": "eve",    "email": "eve@example.com",    "type": "Listener", "subscription": "Premium"},
    {"username": "frank",  "email": "frank@example.com",  "type": "Listener", "subscription": "Free"},
    {"username": "grace",  "email": "grace@example.com",  "type": "Listener", "subscription": "Premium"},
    {"username": "heidi",  "email": "heidi@example.com",  "type": "Listener", "subscription": "Free"},
    {"username": "ivan",   "email": "ivan@example.com",   "type": "Listener", "subscription": "Premium"},
    {"username": "judy",   "email": "judy@example.com",   "type": "Listener", "subscription": "Free"},
]

# Predefined playlists with owner username and songs (by title)
predefined_playlists = [
    {
        "name": "Chill Vibes",
        "owner": "alice",
        "songs": ["Dream On", "Sky High", "Heartbeat"]
    },
    {
        "name": "Workout Hits",
        "owner": "bob",
        "songs": ["Thunder", "Light Up", "Sky High"]
    },
    {
        "name": "Evening Relax",
        "owner": "carol",
        "songs": ["Eclipse", "River", "Shadows"]
    }
]
