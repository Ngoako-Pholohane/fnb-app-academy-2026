learner_name = input("Enter learner's name: ").title()
subject1 = float(input("Enter your subject 1 mark: "))
subject2 = float(input("Enter your subject 2 mark: "))
subject3 = float(input("Enter your subject 3 mark: "))

average_mark = round((subject1 + subject2 + subject3) / 3, 2)

if average_mark >= 80:
    letter_grade = "A"
elif average_mark >= 70:
    letter_grade = "B"
elif average_mark >= 60:
    letter_grade = "C"
elif average_mark >= 50:
    letter_grade = "D"
else:
    letter_grade = "F"


if average_mark >= 50:
    status = "Pass"
else:
    status = "Fail"


if subject1 < 40:
    intervention1 = "Needs Intervention"
else:
    intervention1 = "No Intervention Needed"

if subject2 < 40:
    intervention2 = "Needs Intervention"
else:
    intervention2 = "No Intervention Needed"

if subject3 < 40:
    intervention3 = "Needs Intervention"
else:
    intervention3 = "No Intervention Needed"


print("\n===============LEARNER REPORT CARD===============\n")

print(f"Learner Name          : {learner_name}\n")
print(f"Subject 1 Mark        : {subject1}")
print(f"Subject 2 Mark        : {subject2}")
print(f"Subject 3 Mark        : {subject3}")
print(f"Average Mark          : {average_mark}\n")
print(f"Grade                 : {letter_grade}")
print(f"Status                : {status}\n")
print(f"Subject 1 Intervention: {intervention1}")
print(f"Subject 2 Intervention: {intervention2}")
print(f"Subject 3 Intervention: {intervention3}\n")
print("---------------------------------------------------")
