user_data = {"name": "Rahul", "address": {"city": "Delhi", "pin": "110001"}}

# print(user_data["address"]["city"])
# print(user_data.get("address", {}).get("city", "Unknown"))


# .setdefault()

sentence = "apple banana apple mango banana apple"

# TODO: {'apple': 3, 'banana': 2, 'mango': 1}
words = sentence.split()  # [apple ,banana ,apple ,mango ,banana, apple]

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# print(frequency)

# frequency["apple"] = 1
# frequency["apple"] = 1 + 1 = 2

# frequency = {
#     'apple': 2
# }


# NOTE: dict.setdefault(key, default_value)

# CASE 1: Key EXIST karti hai
# Key ki existing value return karo
# Do not make changes in Dict

# CASE 2: Key EXIST NAHI karti
# Dictionary mein key add karo with default_value
# default_value return karo


student = {"name": "Rahul", "marks": 95}
# print(student)

result = student.setdefault("name", "unknown")  # Rahul

city = student.setdefault("city", "Delhi")  # Delhi
# print(student)
# print(city)


# NOTE: Count Frequency

sentence = "apple banana apple mango banana apple"

words = sentence.split()

frequency = {}

for word in words:
    frequency.setdefault(word, 0)
    frequency[word] += 1

# print(frequency)  # {'apple': 3, 'banana': 2, 'mango': 1}

"""
[apple, banana, apple, mango, banana, apple]

1. word: apple
    setdefault("apple", 0) -> nahi hai -> {"apple": 0}
    frequency["apple"] += 1 -> {"apple": 1}

2. word: banana
   setdefault("banana", 0) -> NO -> {"banana", 0}
   frequency["banana"] += 1 -> {"apple": 1, "banana": 1}

3. word: apple
   setdefault("apple", 0) -> EXIST -> return 1.
   frequency["apple"] += 1 -> {"apple": 2, "banana": 1}
"""

