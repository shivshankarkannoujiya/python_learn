"""
student.txt

Name: Rahul
Roll No: 101
Marks: 95
"""

# open file
# mode: `w`
# 'w' creates the file if it doesn't exist

file = open("student.txt", "w")


# Write content
file.write("Name: Rahul\n")
file.write("Roll No: 101\n")
file.write("Marks: 95\n")

# ALWAYS close the file
file.close()

print("File written successfully!")
