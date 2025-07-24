def total_messages(chats):
    return len(chats)

def unique_users(chats):
    users = []
    for user, _ in chats:
        if user not in users:
            users.append(user)
    return users

def total_words(chats):
    total = 0
    for _, msg in chats:
        total += len(msg.split())
    return total

def average_words(chats):
    if len(chats) == 0:
        return 0
    return total_words(chats) / len(chats)

def longest_message(chats):
    longest = ("", "")
    max_length = 0
    for user, msg in chats:
        if len(msg) > max_length:
            max_length = len(msg)
            longest = (user, msg)
    return longest

def most_active_user(chats):
    counts = {}
    for user, _ in chats:
        if user not in counts:
            counts[user] = 0
        counts[user] += 1
    max_user = ""
    max_count = 0
    for user in counts:
        if counts[user] > max_count:
            max_count = counts[user]
            max_user = user
    print("Most active user:", max_user, "(", max_count, "messages)")

def message_count_user(chats):
    name = input("Enter user name: ").strip()
    count = 0
    for user, _ in chats:
        if user.lower() == name.lower():
            count += 1
    print("Messages sent by", name + ":", count)

def most_frequent_word_user(chats):
    name = input("Enter user name: ").strip()
    words = []
    for user, message in chats:
        if user.lower() == name.lower():
            words += message.lower().split()
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
    max_word = ""
    max_count = 0
    for word in word_count:
        if word_count[word] > max_count:
            max_count = word_count[word]
            max_word = word
    if max_word != "":
        print('Most frequent word used by', name + ': "' + max_word + '"')
    else:
        print("No messages by", name)

def first_last_message(chats):
    name = input("Enter user name: ").strip()
    messages = []
    for user, msg in chats:
        if user.lower() == name.lower():
            messages.append(msg)
    if len(messages) > 0:
        print("First message:", messages[0])
        print("Last message:", messages[-1])
    else:
        print("No messages by", name)

def check_user_present(chats):
    name = input("Enter user name: ").strip().lower()
    found = False
    for user, _ in chats:
        if user.lower() == name:
            found = True
            break
    if found:
        print("User", name, "is present in the chat.")
    else:
        print("User", name, "not found in the chat.")

def repeated_words(chats):
    words = []
    for _, msg in chats:
        words += msg.lower().split()
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
    repeated = []
    for word in word_count:
        if word_count[word] > 1:
            repeated.append(word)
    print("Common repeated words:", repeated)

def longest_avg_message(chats):
    user_lengths = {}
    user_counts = {}
    for user, msg in chats:
        length = len(msg.split())
        if user not in user_lengths:
            user_lengths[user] = 0
            user_counts[user] = 0
        user_lengths[user] += length
        user_counts[user] += 1
    max_avg = 0
    max_user = ""
    for user in user_lengths:
        avg = user_lengths[user] / user_counts[user]
        if avg > max_avg:
            max_avg = avg
            max_user = user
    print("User with longest average message:", max_user, "(", round(max_avg, 2), "words)")

def mention_count(chats):
    name = input("Enter name to check mentions: ").strip().lower()
    count = 0
    for _, msg in chats:
        if name in msg.lower():
            count += 1
    print("Messages mentioning", name + ":", count)

def remove_duplicates(messages):
    seen = []
    for msg in messages:
        if msg not in seen:
            seen.append(msg)
    print("Unique messages count:", len(seen))
    for msg in seen:
        print(msg)

def sort_messages(messages):
    sorted_msgs = sorted(messages)
    print("Messages sorted A-Z:")
    for msg in sorted_msgs:
        print(msg)

def extract_questions(messages):
    questions = []
    for msg in messages:
        if '?' in msg:
            questions.append(msg)
    print("Questions in the chat:")
    for q in questions:
        print(q)

def reply_ratio(chats):
    user1 = input("Enter sender: ").strip().lower()
    user2 = input("Enter replier: ").strip().lower()
    count = 0
    prev_user = ""
    for user, _ in chats:
        if prev_user == user1 and user.lower() == user2:
            count += 1
        prev_user = user.lower()
    print("Reply ratio from", user2, "to", user1 + ":", count, "replies")

def deleted_messages(chats):
    count = 0
    for _, msg in chats:
        if msg.strip().lower() == "this message was deleted":
            count += 1
    print("Deleted messages found:", count)

chats = []

n = int(input("Enter number of messages: "))

for i in range(n):
    line = input("Enter message " + str(i+1) + " (Format: Name:Message): ")
    if ':' in line:
        parts = line.split(":", 1)
        name = parts[0].strip()
        msg = parts[1].strip()
        chats.append((name, msg))

while True:
    print("Select the operation to perform (1-19):")
    print('''1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user1
10. Check if a user is present in the chat
11. Find commonly repeated words
12. Identify the user with the longest average message length
13. Count how many messages mention a specific user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions asked in the chat
17. Calculate the reply ratio between two users
18. Check for deleted messages
0. To Exit
''')

    choice = int(input("Choose your operation to perform: "))

    if choice == 1:
        print("Total messages:", total_messages(chats))

    elif choice == 2:
        print("Unique users in the chat:", unique_users(chats))

    elif choice == 3:
        print("Total words in chat:", total_words(chats))

    elif choice == 4:
        print("Average words per message:", round(average_words(chats), 2))

    elif choice == 5:
        user, message = longest_message(chats)
        print("Longest message sent by", user + ":", message)

    elif choice == 6:
        most_active_user(chats)

    elif choice == 7:
        message_count_user(chats)

    elif choice == 8:
        most_frequent_word_user(chats)

    elif choice == 9:
        first_last_message(chats)

    elif choice == 10:
        check_user_present(chats)

    elif choice == 11:
        repeated_words(chats)

    elif choice == 12:
        longest_avg_message(chats)

    elif choice == 13:
        mention_count(chats)

    elif choice == 14:
        remove_duplicates([msg for _, msg in chats])

    elif choice == 15:
        sort_messages([msg for _, msg in chats])

    elif choice == 16:
        extract_questions([msg for _, msg in chats])

    elif choice == 17:
        reply_ratio(chats)

    elif choice == 18:
        deleted_messages(chats)

    elif choice == 0:
        print("program Exited")
        break

    else:
        print("Option not implemented yet.")
