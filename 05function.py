# Lambda Functions

# def double(x):
#     return x ** 2

# print(double(3))


double = lambda x: x * 2

add = lambda x, y : x + y

# print(double(4))
# print(add(4,3))


students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Priya", "marks": 92},
    {"name": "Ankit", "marks": 78},
    {"name": "Seema", "marks": 95},
]


# lambda s: s["marks"]
# def get_marks(s):
#     return s["marks"]

sorted_students = sorted(students, key=lambda s: s["marks"], reverse=True)


"""
lambda extracts marks -> [85, 92, 78, 95] -> sorted descending -> [95, 92, 85, 78]
"""

# for s in sorted_students:
#     print(f"{s['name']}: {s['marks']}")


