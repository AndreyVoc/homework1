
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
average_grades = {}
for student, grade_list in zip(sorted_students, grades):
    average_grades[student] = sum(grade_list) / len(grade_list)
print(average_grades)