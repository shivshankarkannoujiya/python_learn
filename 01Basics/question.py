# a = 10
# b = 20

# print(f"Value of a: {a}")
# print(f"Value of b: {b}")
# print("Value of b:", b)

# mehtod 1
# temp = a
# a = b
# b = temp
# print(f"Value of a: {a}")
# print(f"Value of b: {b}")

# method 2
# a, b = b, a
# print(f"Value of a: {a}")
# print(f"Value of b: {b}")


# arr = [1, 2, 3, 4, 5, 6]

# count of even numbers

# count = 0

# for i in arr:
#     if i % 2 == 0:
#         count += 1
# print(count)

"""
1: i => if i % 2 == 0:
2: i => if i % 2 == 0: => count = 1
3: i => if i % 2 == 0:
4: i => if i % 2 == 0: => count = 1 + 1
5: i => if i % 2 == 0: 
6: i => if i % 2 == 0: => count = 1 + 1 + 1
"""

arr = [3, 1, 4, 1, 5]

for i in range(len(arr) - 1):
    left = arr[i]
    right = arr[i+1]

    if left > right:
        print(f"{left} > {right} : Left element is greater")
    else:
        print(f"{left} <= {right} →: Right element is greater or equal")
