# Real-World Example: Spotify
# Task 1: Taking inputs from the user

# 1. User phone number (int)
user_phonenumber = int(input("Enter your phone number: "))

# 2. User name (string)
user_name = input("User name: ")

# 3. Monthly subscription price (float)
monthly_subscription = float(input("Monthly subscription price: "))

# 4. Music languages (list)
music_languages = input("Music languages (space-separated): ").split()

# 5. Favourite artists (tuple)
favourite_artists = tuple(input("Enter your favourite artists (comma-separated): ").split(','))

# 6. Premium features (set)
premium_features = set(input("Premium features (coma-separated): ").split(','))

# 7. Downloaded songs with details (dictionary)
downloaded_songs = eval(input("Songs with their details (dictionary format): "))

# 8. Premium subscriber status (bool)
premium_subscriber = bool(int(input("Premium subscriber? (1 for Yes, 0 for No): ")))


# Sample Input Values:
# Enter your phone number: 9876543210
# User name: Dinesh-koda
# Monthly subscription price: 129.9
# Music languages (space-separated): English Hindi Telugu
# Enter your favourite artists (comma-separated): Arijit Singh,SP Balasubrahmanyam,Taylor Swift
# Premium features (comma-separated): Offline Play,High Quality Audio,Ad-Free
# Songs with their details (dictionary format): {"Butta Bomma": {"Language": "Telugu", "Artist": "Armaan Malik", "Duration": "3:18"}, "Tum Hi Ho": {"Language": "Hindi", "Artist": "Arijit Singh", "Duration": "4:22"}, "Samajavaragamana": {"Language": "Telugu", "Artist": "Sid Sriram", "Duration": "3:44"}, "Shape of You": {"Language": "English", "Artist": "Ed Sheeran", "Duration": "4:24"}}
# Premium subscriber? (1 for Yes, 0 for No): 1


# Task 2: Display details using different formatting methods

# 1. Comma-separated output
print("User phone number:", user_phonenumber, "User name:", user_name, "Premium subscriber?:", premium_subscriber, sep=', ')
#output:User phone number:, 9876543210, User name:, Dinesh-koda, Premium subscriber?:, True

# 2. Percentage formatting (using % operator)
print("Monthly Subscription: %.2f" % monthly_subscription)
#output:Monthly Subscription: 129.90  

# 3. Using f-strings (formatted string literals)
print(f"Music languages: {music_languages}")
print(f"Favourite artists: {favourite_artists}")
print(f"Premium features: {premium_features}")
'''output:
Music languages: ['English,Hindi,Telugu']
Favourite artists: ('Arijit Singh', 'SP Balasubrahmanyam', 'Taylor Swift')
Premium features: {'High Quality Audio', 'Ad-Free', 'Offline Play'}''' 

# 4. Using str.format() method
print("Downloaded songs and details: {}".format(downloaded_songs))
'''output:
Downloaded songs and details:
 {
 'Butta Bomma': {'Language': 'Telugu', 'Artist': 'Armaan Malik', 'Duration': '3:18'}, 
'Tum Hi Ho': {'Language': 'Hindi', 'Artist': 'Arijit Singh', 'Duration': '4:22'},
'Samajavaragamana': {'Language': 'Telugu', 'Artist': 'Sid Sriram', 'Duration': '3:44'},
'Shape of You': {'Language': 'English', 'Artist': 'Ed Sheeran', 'Duration': '4:24'}
}'''
