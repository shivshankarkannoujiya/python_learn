# NOTE: .copy() — Shallow Copy


# original = {"name": "Rahul", "marks": 95}

# fake_copy = original

# print("ORIGINAL: ", id(original))  # 2082383408256
# print("FAKE_COPY: ", id(fake_copy))  # 2082383408256


# fake_copy["marks"] = 100
# print(fake_copy["marks"])  # 100
# print(original["marks"])  # 100


original_dict = {"name": "Rahul", "marks": 95}

real_copy = original_dict.copy()

# print("original id: ", id(original_dict))  # 2540426767488
# print("real_copy id: ", id(real_copy))  # 2540424114752

real_copy["marks"] = 0

# print(real_copy["marks"])  #  0
# print(original_dict["marks"])  # 95


# NOTE: LIMITATION: SHALLOW

# student = {"name": "Rahul", "address": {"city": "Delhi", "pin": "110001"}}

# student_copy = student.copy()

# OUTER LEVEL

# student["name"] = "Priya"
# print(student["name"])  # Priya
# print(student_copy["name"])  # Rahul

# student_copy["address"]["city"] = "Mumbai"

# print(student_copy["address"]["city"])  # Mumbai
# print(student["address"]["city"])  # Mumbai


# NOTE: deepcopy()
import copy

student = {"name": "Rahul", "address": {"city": "Delhi", "pin": "110001"}}

student_copy = copy.deepcopy(student)

student["address"]["city"] = "Mumbai"

# print(student["address"]["city"])  # Mumbai
# print(student_copy["address"]["city"])  # Delhi


# TODO: .fromkeys()

# dict.fromkeys(keys, default_value)

# keys ->  Iterable (list, tuple, string)
# default_value → Har key ki value (default: None)

subjects = ["Math", "Science", "English", "Hindi"]

# {"Math": 0, "Science": 0, "English": 0, "Hindi": 0}

marks = dict.fromkeys(subjects, 0)
# print(marks)

keys = [100, 200,300] 
values = [1,2,3,4]

d1 = dict.fromkeys(keys, values)

# print(d1)

