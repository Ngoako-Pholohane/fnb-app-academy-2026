num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2


print("\n========== RESULTS ==========")
print(f"Addition: {round(addition, 2)}")
print(f"Substraction: {round(subtraction, 2)}")
print(f"Multiplication: {round(multiplication, 2)}")

if num2 == 0:
    print("Division      : Cannot divide by zero")
    print("Floor Division: Cannot divide by zero")
    print("Modulus       : Cannot divide by zero")
else:
    division = num1 / num2
    floor_division = num1 // num2
    modulus = num1 % num2

    print(f"Division      : {round(division, 2)}")
    print(f"Floor Division: {round(floor_division, 2)}")
    print(f"Modulus       : {round(modulus, 2)}")
