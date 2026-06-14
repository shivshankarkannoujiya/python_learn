student = {"name": "Rahul", "age": 20, "city": "Delhi", "marks": 95, "passed": True}


# for key in student:
#     print(key)

"""
name
age
city
marks
passed
"""

# .keys()

# for key in student.keys():
#     print(key)


# TODO: name --> Rahul
# for key in student.keys():
#     print(key, "-->", student[key])


# for key in student:
#     print(student[key])

# .values() method
# for value in student.values():
#     print(value)


# class_marks = {
#     "Rahul" : 95,
#     "Priya" : 87,
#     "Amit"  : 76,
#     "Sneha" : 92,
#     "Karan" : 55
# }

# total = 0

# for marks in class_marks.values():
#     total = total + marks

# average = total / len(class_marks)
# print(average)


student = {"name": "Rahul", "age": 20, "city": "Delhi", "marks": 95, "passed": True}

# .items()

# for key, value in student.items():
#     print(key, " : ", value)


# print(student.items())
"""
dict_items(
    [
        ("name", "Rahul"), ("age", 20), ("city", "Delhi"), ("marks", 95), ("passed", True)
    ]
)
"""


# pair = ("name", "Rahul")
# key , value = pair

# print(key)
# print(value)


# for index, (key, val) in enumerate(student.items()):
#     print(f"{index }. {key} = {val}")


school = {
    "Rahul": {"age": 20, "marks": 95, "city": "Delhi"},
    "Priya": {"age": 19, "marks": 87, "city": "Mumbai"},
    "Amit": {"age": 21, "marks": 76, "city": "Pune"},
}

# for student_name, student_info in school.items():
#     print(f"\nStudent: {student_name}")

#     for key, value in student_info.items():
#         print(f"{key} : {value}")


"""
.setdefault()
.update()
.copy()
.copy.deepcopy()
.fromkeys()
"""
