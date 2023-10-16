# Selecting Sort

# more clear variant


def selectingSort_1(arr):
    result_arr = []
    for j in range(len(arr)):
        smallest_num = arr.index(min(arr))  # find index of the smallest number in array
        result_arr.append(arr.pop(smallest_num))

    return result_arr


def selectingSort_2(arr):
    result_arr = []
    for j in range(len(arr)):
        result_arr.append(arr.pop(arr.index(min(arr))))
    return result_arr



print(selectingSort_1([9, 2, 4, 1, 0, 5, 6]))
print(selectingSort_2([9, 2, 4, 1, 0, 5, 6]))




# Quick Sort

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [j for j in arr[1::] if j <= pivot]
        greater = [j for j in arr[1::] if j > pivot]
    return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([9, 2, 4, 1, 0, 5, 6]))



# BogoSort
import random
def bogoSort(arr):
    while not sorted(arr) == arr:
        random.shuffle(arr)
    return arr
print(bogoSort([9, 2, 4, 1, 0, 5, 6]))
