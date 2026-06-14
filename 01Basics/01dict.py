my_dict = {}

my_dict = dict()

# print(type(my_dict))  # <class 'dict'>
# print(my_dict)  # {}


student = {
    "name": "Manas",
    "age": 20,
    "city": "abc",
    "marks": 97,
    "passed": True 
}

# print(id(student))
# print(student)
# student = dict(name="Rahul", age=20, city="Delhi")

# NOTE: Mutable

student["marks"] = 100
# print(student)
# print(id(student))


# Key of Dict should be unique and Immutable
dict1 = {
    "name": "abhi",
    "name": "Abhishek"
}

# print(dict1)


