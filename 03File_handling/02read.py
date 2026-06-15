# Open file in read mode
file = open("student.txt", "r")

# Read the entire content as one string
content = file.read()

file.close()

print(content)