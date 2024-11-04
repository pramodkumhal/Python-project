# Empty dictionary to store contacts
contact = {}

while True:
    print("\nContact Book App")
    print("1. Create contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contacts")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":  # Create contact
        name = input("Enter your name: ")
        if name in contact:
            print(f"Contact name {name} already exists!")
        else:
            age = input("Enter age: ")
            email = input("Enter email: ")
            mobile = input("Enter mobile number: ")
            contact[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f"Contact name {name} has been created successfully!")

    elif choice == '2':  # View contact
        name = input("Enter contact name to view: ")
        if name in contact:
            contact_details = contact[name]
            print(f"Name: {name}, Age: {contact_details['age']}, Mobile number: {contact_details['mobile']}, Email: {contact_details['email']}")
        else:
            print("Contact not found!")

    elif choice == '3':  # Update contact
        name = input("Enter contact name to update: ")
        if name in contact:
            age = input("Enter updated age: ")
            email = input("Enter updated email: ")
            mobile = input("Enter updated mobile number: ")
            contact[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f"Contact name {name} has been updated successfully!")
        else:
            print("Contact not found!")

    elif choice == '4':  # Delete contact
        name = input("Enter contact name to delete: ")
        if name in contact:
            del contact[name]
            print(f"Contact name {name} has been deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == '5':  # Search contact
        search_name = input("Enter contact name to search: ")
        found = False
        for name, details in contact.items():
            if search_name.lower() in name.lower():
                print(f"Found - Name: {name}, Age: {details['age']}, Mobile Number: {details['mobile']}, Email: {details['email']}")
                found = True
        if not found:
            print("No contact found with that name.")

    elif choice == '6':  # Count contacts
        print(f"Total contacts in your book: {len(contact)}")

    elif choice == '7':  # Exit program
        print("Goodbye... Closing the program.")
        break

    else:
        print("Invalid Input! Please enter a number between 1 and 7.")