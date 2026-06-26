students = []

n = int(input())

for _ in range(n):
    name = input()
    grade = float(input())

    students.append([name, grade])

grades = [student[1] for student in students]

second_lowest = sorted(set(grades))[1]

names = []

for student in students:
    if student[1] == second_lowest:
        names.append(student[0])

names.sort()

for name in names:
    print(name)