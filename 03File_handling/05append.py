# 'a' mode — adds to end WITHOUT destroying existing content

file = open("student.txt", "a")
file.write("City: Lucknow\n")
file.close()


# verify

file = open("student.txt", "r")
content = file.read()
print(content)

file.close()



