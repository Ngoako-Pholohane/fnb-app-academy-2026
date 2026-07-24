secret_password = input("Enter your secret password: ").strip()

first_letter = secret_password[0].upper()
last_letter = secret_password[-1].upper()

print(f"\nYour password hint: It starts with {first_letter} and ends with {last_letter}\n")
