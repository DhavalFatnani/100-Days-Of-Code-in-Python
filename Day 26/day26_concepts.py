import random

# LIST COMPREHENSION
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
name = "Dhaval"
letter_list = [letter for letter in name]
numbers_list = [1, 2, 3, 4]
manipulated_list = [n * 2 for n in range(1, 5)]
names = ["Dhaval", "Hasti", "Sahil", "Dev", "Neil"]
short_names = [name for name in names if len(name) < 5]
capital_long_names = [name.upper() for name in names if len(name) > 4]

# DICTIONARY COMPREHENSION
names = ["Dhaval", "Hasti", "Archi", "Sahil", "Dev", "Neil"]
student_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}

print(student_scores)
print(passed_students)
