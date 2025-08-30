import os
import re

# Path where notes will be stored
NOTES_DIR = "usernotes"

# Predefined sentiment word lists
positive_words = ["good", "great", "excellent", "happy", "love", "fantastic", "positive", "success"]
negative_words = ["bad", "sad", "poor", "angry", "hate", "terrible", "negative", "failure"]

# Ensure notes directory exists
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

def analyze_sentiment(content):
    pos_count = 0
    neg_count = 0

    for word in positive_words:
        matches = re.findall(rf"\b{word}\b", content, re.IGNORECASE)
        pos_count += len(matches)

    for word in negative_words:
        matches = re.findall(rf"\b{word}\b", content, re.IGNORECASE)
        neg_count += len(matches)

    if pos_count > neg_count:
        return "Positive 😊"
    elif neg_count > pos_count:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def analyze_notes():
    files = os.listdir(NOTES_DIR)
    if not files:
        print("No notes found.")
        return

    print("\nAvailable notes:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

    choice = input("Enter note number to analyze (or 'all' for all notes): ")

    if choice.lower() == "all":
        for file in files:
            with open(os.path.join(NOTES_DIR, file), "r") as f:
                content = f.read()
                sentiment = analyze_sentiment(content)
                print(f"\n--- {file} ---")
                print(content)
                print(f"Sentiment: {sentiment}")
    else:
        try:
            idx = int(choice) - 1
            filename = files[idx]
            with open(os.path.join(NOTES_DIR, filename), "r") as f:
                content = f.read()
                sentiment = analyze_sentiment(content)
                print(f"\n--- {filename} ---")
                print(content)
                print(f"Sentiment: {sentiment}")
        except (ValueError, IndexError):
            print("Invalid choice.")

def create_note():
    filename = input("Enter new note filename (with .txt): ")
    filepath = os.path.join(NOTES_DIR, filename)

    if os.path.exists(filepath):
        print("Note already exists! Try modifying instead.")
        return

    content = input("Enter your note content:\n")
    with open(filepath, "w") as f:
        f.write(content)
    print("Note created successfully!")

def modify_note():
    files = os.listdir(NOTES_DIR)
    if not files:
        print("No notes found to modify.")
        return

    print("\nAvailable notes:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

    try:
        choice = int(input("Enter note number to modify: ")) - 1
        filename = files[choice]
        filepath = os.path.join(NOTES_DIR, filename)

        with open(filepath, "r") as f:
            old_content = f.read()
        print("\nCurrent content:\n", old_content)

        new_content = input("\nEnter new content (this will overwrite existing):\n")
        with open(filepath, "w") as f:
            f.write(new_content)

        print("Note modified successfully!")
    except (ValueError, IndexError):
        print("Invalid choice.")

def main():
    while True:
        print("\n--- Intelligent Notes Management System ---")
        print("1. Analyze Notes")
        print("2. Create New Note")
        print("3. Modify Existing Note")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            analyze_notes()
        elif choice == "2":
            create_note()
        elif choice == "3":
            modify_note()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
