contacts = {
    "Convy": "0712345678",
    "Simon": "0823456789",
    "Lesley": "0798765432"
}

name = input("\nWhich friend's number do you want to look up? ").title()

if name in contacts:
    phone = contacts[name]
    print(f"\nFound! {name}'s number is {phone}.")
else:
    print("Contact not found.")
