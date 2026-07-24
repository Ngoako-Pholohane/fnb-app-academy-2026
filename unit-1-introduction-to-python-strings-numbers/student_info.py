first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
fav_number = float(input("Enter your favourite number: "))

full_name = f"{first_name} {surname}"

uppercase_name = full_name.upper()
title_case_name = full_name.title()
age_in_months = age * 12
rounded_fav_number = round(fav_number, 2)


print("\n================= RESULTS =================\n")

print(f"Welcome, {full_name}\n")

print(f"Name                    : {full_name}")
print(f"Uppercase Name          : {uppercase_name}")
print(f"Title Case Name         : {title_case_name}\n")

print(f"Age                     : {age}")
print(f"Age in Months           : {age_in_months}\n")

print(f"Favourite Number        : {fav_number}")
print(f"Rounded Favourite Number: {rounded_fav_number}\n")

print("----------DATA TYPES----------")
print(f"First Name      : {type(first_name)}")
print(f"Surname         : {type(surname)}")
print(f"Age             : {type(age)}")
print(f"Favourite Number: {type(fav_number)}\n")

print("=============================================")
