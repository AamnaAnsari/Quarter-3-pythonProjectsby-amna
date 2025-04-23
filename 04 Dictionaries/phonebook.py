# Create an empty phonebook dictionary
phonebook = {}

while True:
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. View Phonebook")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phonebook[name] = number
        print(f"{name} added to phonebook.")

    elif choice == "2":
        print("\nPhonebook Contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
