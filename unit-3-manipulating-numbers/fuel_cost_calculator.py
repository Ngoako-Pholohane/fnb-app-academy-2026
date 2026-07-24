kilometers = float(input("How many kilometers do you want to drive? "))
petrol_price = float(input("What is the current petrol price per liter? "))

liters_needed = kilometers / 10
total_cost = liters_needed * petrol_price

print(f"\nTotal Fuel Cost: R{round(total_cost, 2)}")
