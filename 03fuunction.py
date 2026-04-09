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


def print_result(name, marks):

    # calculate grade
    grade = calculate_grade(marks)

    print("-" * 30)
    print(f"Student: {name}")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print("-" * 30)


print_result("Manas", 85)
print_result("Abhi", 95)
print_result("Priya", 90)
