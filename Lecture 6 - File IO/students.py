import csv

students = []

with open('students.csv') as file:
    for row in csv.DictReader(file):
        students.append({'name': row['name'], 'home': row['home']})
    # for line in file:
    #     name, home = line.rstrip().split(',')
    #     students.append({ 'name': name, 'home': home })

for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} is from {student['home']}")