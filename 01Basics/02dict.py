# [] / .get()

# student = {"name": "Rahul", "age": 20, "city": "Delhi", "marks": 95}

# print(student["name"])
# print(student["marks"])

# print(student["phone"])  # KeyError: 'phone'


# dict.get()


# print(student.get("phone"))  # None
# print(student.get("phone", "Number does not exist"))

# print(student.get("marks", 0))


# TODO: CREATE & UPDATE

# student = {"name": "Rahul", "marks": 95}
# print(student)


# NOTE: add new key-value
# student["city"] = "Delhi"
# student["phone"] = "9876543210"
# print(student)


# Update existing key
# student["marks"] = 99
# print(student.get("marks"))


# .update() Method

# student = {"name": "Rahul", "marks": 95}

# student.update({
#     "marks": 99,
#     "city": "Delhi",
#     "phone": "125475676365"
# })

# print(student)


dict1 = {"name": "Rahul", "age": 20}
dict2 = {"city": "Delhi", "marks": 95}

# dict1.update(dict2)
# print(dict1)


# NOTE: del keyword
del dict1["age"]
# print(dict1)

# .pop()
# student = {
#     "name"  : "Rahul",
#     "age"   : 20,
#     "city"  : "Delhi",
#     "marks" : 95
# }

# removed_city = student.pop("city")

# print(removed_city)
# print(student)

# removed_phone = student.pop("phone", "Not Found")
# removed_phone = student.pop("marks", "Not Found")
# print(removed_phone)


# NOTE: .popitem() => Delete last item
student = {
    "name"  : "Rahul",
    "age"   : 20,
    "city"  : "Delhi",
    "marks" : 95
}

# last_item = student.popitem()
# print(last_item)


# NOTE: .clear()

# student.clear()
# print(student)  # {}


# l1 = [1,2,3,4]
# l1.clear()
# print(l1)  # []



