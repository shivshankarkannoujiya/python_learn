def birthday_party(*guests):
    print(f"Total guests: {len(guests)}")
    for guest in guests:
        print(f"Welcome, {guest}! 🎉")


# birthday_party("Rahul")
# birthday_party("Priya", "Ankit")
# birthday_party("ankit", "ajay", "abhay")  # ('ankit', 'ajay', 'abhay')


def total_sum(*num):
    print(num)
    result = 0
    for n in num:
        result += n
    return result


# print(total_sum(1, 2))
# print(total_sum(10, 20, 30))
# print(total_sum(1, 2, 3, 4, 5))


# NOTE: **kwargs
"""
=== User Profile ===
name: Rahul
age: 22
city: Delhi
hobby: Cricket
"""

def create_profile(**details):
    print("=== User Profile ===")
    for key, value in details.items():
        print(f"{key}: {value}")


# create_profile(name="Rahul", age=22, city="Delhi", hobby="Cricket")

def ultimate_function(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

# ultimate_function(1, 2, 3, 4, name="Rahul", age=22, city="Delhi")


