n = int(input("Enter terms: "))

a, b = 0, 1

for i in range(n):

    print(a, end=" ")

    a, b = b, 2 * b + a
