students = [
    {
        "name": "convy",
        "maths": 85,
        "english": 78,
        "science": 90
    },
    {
        "name": "simon",
        "maths": 65,
        "english": 72,
        "science": 68  
    },
    {
        "name": "lesley",
        "maths": 45,
        "english": 50,
        "science": 48
    },
    {
        "name": "bridget",
        "maths": 92,
        "english": 88,
        "science": 95
    },
    {
        "name": "johannah",
        "maths": 35,
        "english": 40,
        "science": 30
    }
]

results = []

total_average = 0
highest_average = 0
lowest_average = 100

for student in students:
    average = round((student["maths"] + student["english"] + student["science"]) / 3, 2)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"
    
    report = {
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    }

    results.append(report)

    total_average += average

    if average > highest_average:
        highest_average = round(average, 2)
    if average < lowest_average:
        lowest_average = round(average, 2)


class_average = total_average / len(students)

print("\n===============CLASS REPORT===============\n")

for result in results:
    print("-----------------------------------------")
    print(f"Learner Name          : {result['name'].title()}")
    print(f"Average Mark          : {result['average']}")
    print(f"Grade                 : {result['grade']}")
    print(f"Status                : {result['status']}")

print("\n===============CLASS STATISTICS===============\n")

print(f"Class Average  : {class_average}")
print(f"Highest Average: {highest_average}")
print(f"Lowest Avearge : {lowest_average}")
print("---------------------------------------------------")

while True:
    search = input("Enter a student's name to search (or type 'exit'): ").lower()

    if search == "exit":
        print("Goodbye!")
        break

    found = False

    for result in results:
        if search == result["name"]:
            print("\nStudent Found.")
            print(f"Learner Name          : {result['name'].title()}")
            print(f"Average Mark          : {result['average']}")
            print(f"Grade                 : {result['grade']}")
            print(f"Status                : {result['status']}\n")

            found = True
            break

    if found == False:
        print("Student Not Found.")
