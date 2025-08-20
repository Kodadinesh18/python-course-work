
import allprograms

# Mapping choices to functions
all_programs = {
    1: allprograms.kadane_algorithm,
    2: allprograms.factors_of_number,
    3: allprograms.prime_factors,
    4: allprograms.strong_number,
    5: allprograms.merge_sorted_arrays,
    6: allprograms.perfect_square,
    7: allprograms.automorphic_number,
    8: allprograms.harshad_number,
    9: allprograms.abundant_number,
    10: allprograms.friendly_pair
}

def display_menu():
    print("------ FUNCTION MENU ------")
    print("1. Power of a Number")
    print("2. Factors of a Number")
    print("3. Prime Factors")
    print("4. Strong Number")
    print("5. Perfect Number")
    print("6. Perfect Square")
    print("7. Automorphic Number")
    print("8. Harshad Number")
    print("9. Abundant Number")
    print("10. Friendly Pair")
    print("0. Exit")
    print("----------------------------")

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Exiting...")
            break
        elif choice in all_programs:
            all_programs[choice]()
        else:
            print("Invalid choice. Try again.")
    except ValueError:
        print("Please enter a valid number.")
