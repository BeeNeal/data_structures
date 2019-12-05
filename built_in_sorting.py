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
# stable - if key is the same, then original order is preserved

# key functions don't need to depend directly on objects being sorted - can
# take external resource
fruits = ['apple', 'cherry', 'berry']
sugar_content = {'apple':12, 'cherry':16, 'berry':6 }
print(sorted(fruits, key=sugar_content.__getitem__))