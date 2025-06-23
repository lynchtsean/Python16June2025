def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

students = []

num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    print(f"\nStudent {i + 1}:")
    name = input("Enter the student's name: ")
    score = int(input("Enter the student's score (0–100): "))

    grade = check_grade(score)

    students.append((name, grade))

    print(f"{name} got a grade of {grade}")

print("\n Final Grades List:")
for name, grade in students:
    print(f"{name}: {grade}")