n = int(input("Enter the terms: "))

a, b = 2, 1

for i in range(n):

    print(a, end=" ")

    a, b = b, a + b
