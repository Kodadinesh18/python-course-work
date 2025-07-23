def total_messages(chats):
    return len(chats)

def unique_users(chats):
    names = []
    for i in chats:
        name = i[0]
        names.append(name)
    names = set(names)
    return names

def total_words(chats):
    count=0
    for names,messages in chats:
        words=messages.strip().split()
        count+=len(words)
    return count
def average_words(chats):
    total_messages=len(chats)
    count=0
    for names,messages in chats:
        words=messages.strip().split()
        count+=len(words)
    average=count/total_messages
    return average

def longest_message(chats):
    max_length=0
    longest=("","")
    for user,message in chats:
        if len(message)>max_length:
            max_length=len(message)
            longest=(user,message)
    return longest

def most_active(chats):
    
        

n = int(input("enter the number of messages: "))
chats = []
for i in range(n):
    message = tuple(input().split(":", 1))  # Added '1' to handle colons in messages
    chats.append(message)


while True:
    print("select the operation to perform(1-19)")
    print('''1. Count total number of messages
             2. Identify unique users in the chat
             3. Count total words in the chat
             4. Calculate average words per message
             5. Find the longest message sent
             6. Find the most active user
             7. Get message count for a specific user
             8. Find the most frequently used word by a specific user
             9. Retrieve the first and last message sent by a user
             10. Check if a user is present in the chat
             11. Find commonly repeated words
             13. Identify the user with the longest average message length
             14. Count how many messages mention a specific user
             15. Remove duplicate messages
             16. Sort messages alphabetically
             17. Extract all questions asked in the chat
             18. Calculate the reply ratio between two users
             19. Check for deleted messages
             0. To Exit
             ''')
    choice = int(input("choose your operation to perform:"))

    if choice == 1:
        print("Total messages:", total_messages(chats))
    elif choice == 2:
        print("Unique users in the chat:", unique_users(chats))
    elif choice == 3:
        print("Total words in chat:", total_words(chats))
    elif choice== 4:
        print("Average words per message:",average_words(chats))
    elif choice==5:
         user, message = longest_message(chats)
    print(f"Longest message sent by {user}:{message}")

    elif choice == 0:
        print("Exiting program...")
        break
    else:
        print("Option not implemented yet.")
