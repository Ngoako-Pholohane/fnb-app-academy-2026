first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio message: ").strip()

username = f"{first_name[0].lower()}{last_name.lower()}"

full_name = f"{first_name} {last_name}"
title_case_name = full_name.title()

characters_in_bio = len(bio)
new_bio = bio.replace("I am", "I'm")


print(f"\nFull Name                      : {title_case_name}")
print(f"Username                       : {username}")
print(f"Cleaned Bio                    : {new_bio}")
print(f"Number of Characters in the Bio: {characters_in_bio}")
