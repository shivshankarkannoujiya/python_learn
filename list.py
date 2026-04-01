"""
🛒 My Shopping List:
- Apples
- Milk
- Bread
- Eggs
"""

# f1 = "apple"
# f1 = "Milk"
# f1 = "Bread"
# f1 = "Eggs"

# shopping_list = ["apple", "milk", "bread"]
# l1 = ["milk", True, 12, 1.4]

name = "manas"

# NOTE: list()

# name_list = list(name)
# print(name_list)

# fruits = ["Apple", "Mango", "Banana", "Orange"]
# index     0         1        2         3

# TODO:  Access Element
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])

# fruits = ["Apple", "Mango", "Banana", "Orange"]
#   -4       -3       -2        -1

# print(fruits[-1])

# NOTE: Slicing

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]
#           0        1         2         3         4

# start -> lastIndex - 1
# print(fruits[0:3])
# print(fruits[:3])

# negative_index = length_of_list + given_negative_index
# print(fruits[-2:])
# print(fruits[3:])

# animals = ["Cat", "Dog", "Elephant", "Tiger", "Lion"]
# print(animals[-1:])


# Modify
# colors = ["Red", "Blue", "Green"]
# print(colors)

# colors[1] = "Yellow"
# print(colors)

# append(): add element at last
# shopping = ["Milk", "Bread"]
# shopping.append("abc")
# print(shopping)

# shopping = ["Milk",  "Bread", "Eggs"]
#         #     0        1        2
# shopping.insert(1, "butter")


# fruits = ["Apple", "Mango", "Banana"]
# fruits.remove("Mango")


# pop()
# default index = -1
# fruits = ["Apple", "Mango", "Banana"]
# deletedElem = fruits.pop()
# print(deletedElem)

# del:  Delete by position or the whole list
# fruits = ["Apple", "Mango", "Banana", "Orange"]

# del fruits[0]
# print(fruits)

# del fruits
# print(fruits)


# list1 = ["Apple", "Mango"]
# list2 = ["Banana", "Orange"]

# combined = list1 + list2
# print(combined)

# ['Apple', 'Mango', 'Banana', 'Orange']

# fruits = ["Apple", "Mango", "Banana"]
# print("Mango" in fruits)


# invited_guests = ["Riya", "Amit", "Kavya", "manas"]

# name = input("Enter: ")

# if name in invited_guests:
#     print(name, "Invited")
# else:
#     print(name, "is not Invited")

# l1 = [1,2,3,4,5,6,7]

# for a in l1:
#     print(a, end=" ")

fruits = ["Apple", "Mango", "Banana"]

# for f in fruits:
#     print(f)

# 0: Apple
# 1: Mango
# 2: Banana

# for f in range(0, len(fruits)):
#     print(f, "->", fruits[f])


# numbers = [5, 2, 8, 1, 9]
# numbers.sort()

# names = ["Zara", "Alice", "Mike"]
# name.sort()

# numbers = [1, 2, 3, 4, 5]
# numbers.reverse()

# numbers = [1, 2, 2, 3, 2, 4]
# print(numbers.count(2))

# fruits = ["Apple", "Mango", "Banana"]
# print(fruits.index("Mango"))

# my_list = [1, 2, 3, 4]
# my_list.clear()
# print(my_list) #


# classroom = [
#     ["Riya", "Amit", "Dev"],  # Row 0
#     ["Priya", "Kavya", "Raj"],  # Row 1
#     ["Sneha", "Arjun", "Meera"],  # Row 2
# ]

# print(classroom[0][1])  # ['Riya', 'Amit', 'Dev']
# print(classroom[1])
# print(classroom[2])


# board = [
#     ["X", "O", "X"],
#     ["O", "X", "O"],
#     ["X", "X", "O"]
# ]

# for i in board:
#     print(i)


# numbers = []
# [1,2,3,4,5]

# sum_of_numbers = 0
# for i in range(len(numbers)):
#     sum_of_numbers += numbers[i]

# print(sum_of_numbers)

# for i in range(1,6):
#     numbers.append(i)
# [1,2,3,4,5]


# numbers = [i for i in range(1,6)]

# print(numbers)

# squares = [i * i for i in range(1, 6)]

# sq = []

# for i in range(1,6):
#     sq.append(i*i)

# squares = [i * i for i in range(1, 6)]


l = [1, 2, 5, 9, 7, 8, 4, 5, 3, 6, 4, 5, 10]
# l.sort(reverse=False)
# print(l)

sorted_list = sorted(l, reverse=False)
print(sorted_list)
print(l)