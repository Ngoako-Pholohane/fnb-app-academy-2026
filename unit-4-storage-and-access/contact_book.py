contacts = []


def add_contact():
    name = input("Enter name: ").lower()
    phone = input("Enter phone number:")
    email = input("Enter email address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)


def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return None


def delete_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            return


def view_all():
    for contact in contacts:
        print(f"Name: {contact['name'].title()}")
        print(f"Phone:{contact['phone']}")
        print(f"Email: {contact['email']}\n")


while True:
    print("\n==========CONTACT BOOK==========\n")
    print("-----MENU-----")
    print("1. Add")
    print("2. Search")
    print("3. Delete")
    print("4. View all")
    print("5. Exit\n")

    choice = input("Choose an action (1-5): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        name = input("Enter the contact name you want to search: ").lower()
        result = search_contact(name)
        if result:
            print("\nContact found:")
            print(f"Name: {result['name'].title()}")
            print(f"Phone:{result['phone']}")
            print(f"Email: {result['email']}")
        else:
            print("\nContact not found.")


    elif choice == "3":
        name = input("Enter the contact name you want to delete: ").lower()
        delete_contact(name)

    elif choice == "4":
        view_all()

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
