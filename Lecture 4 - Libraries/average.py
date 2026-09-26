import statistics

grades = [8, 7, 8, 9, 10, 5, 7]
average_grade = round(statistics.mean(grades), 2)

print('grades', grades, sep=': ')
print('average grade', average_grade, sep=': ')