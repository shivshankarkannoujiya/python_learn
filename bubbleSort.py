arr = [5, 3, 8, 1, 2]

n = len(arr)

# OUTER LOOP: Kitne passes lagenege
# n = 5
# n-1 : 0, 1, 2, 3, | 4

for i in range(n - 1):  # 0, 1, 2, 3, | 4

    # Inner Loop: Pass me kya krna hai.
    for j in range(n - 1 - i):

        # COMPARISON: Check swap karna hai ki nhi
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted list: ", arr)
