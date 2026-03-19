contact = {}
while True:
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter contact name:")
        number = input("Enter contact number:")
        contact[name] = number
        print("Contact added successfully.")
    elif choice == "2":
        if not contact:
            print("No contacts found.")
        else:
            for name, number in contact.items():
                print(f"Name: {name}, Number: {number}")
    elif choice == "3":
        search_name = input("Enter contact name to search:")
        if search_name in contact:
            print(f"Name: {search_name}, Number: {contact[search_name]}")
        else:
            print("Contact not found.")
    elif choice == "4":
        print("Exiting the contact book. Goodbye!")
        break