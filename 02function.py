def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"


# marks = int(input("Marks: "))
# result = calculate_grade(marks)
# print("RESULT: ", result)


# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")


# greet("Manas", "Namaste")
# greet("Manas")
