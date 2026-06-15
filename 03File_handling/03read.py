file = open("student.txt", "r")

file.seek(0)

line1 = file.readline()
line2 = file.readline()


file.close()

print(line1)
print(line2)

