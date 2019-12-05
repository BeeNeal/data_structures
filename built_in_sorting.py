student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
        ('jane', 'B', 13)
        ]
# 
sorted_students = sorted(student_tuples, key=lambda student: student[1])
print(sorted_students)
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10), ('jane', 'B', 13)]
# if key is the same, then takes in original order