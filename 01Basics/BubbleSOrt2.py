arr = [5, 3, 8, 1, 2]
# arr = [1, 2, 3, 4, 5]

n = len(arr)


for i in range(n - 1):

    isSwapped = False

    for j in range(n - 1 - i):

        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

            isSwapped = True
    print(f"Pass {i} done. Swapped: {isSwapped}")

    if not isSwapped:
        print("List already Sorted..")
        break


print("Sorted list: ", arr)
