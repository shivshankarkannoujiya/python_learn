# 1. STATISTICS MODULE
# NOTE: mean()


import statistics

marks = [45, 67, 89, 90, 55]

avg = statistics.mean(marks)
# print("Average marks: ", avg)


"""
length = len(marks)
total_sum = 0

for i in marks:
    total_sum += i

average_marks = total_sum / length
print(average_marks)
"""


# NOTE: median()
marks_one = [45, 67, 89, 90, 55]

middle_val = statistics.median(marks_one)
# print(middle_val)


# NOTE: mode()

marks_two = [45, 67, 45, 90, 55, 45]

most_repeated = statistics.mode(marks_two)
print(most_repeated)
