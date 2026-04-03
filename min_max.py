numbers = [4, 7, 1, 9, 2, 6]

largest = numbers[0]

smallest = numbers[0]

for num in numbers:

    if num > largest:

        largest = num

    if num < smallest:

        smallest = num

print("LARGEST: ", largest)
print("SMALLEST: ", smallest)
