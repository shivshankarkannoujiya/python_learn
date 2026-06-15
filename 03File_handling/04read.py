file = open("student.txt", "r")

lines = file.readlines()

print(lines)
print(type(lines))  # ['Name: Rahul\n', 'Roll No: 101\n', 'Marks: 95\n', '\n']

file.close()
