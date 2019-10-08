# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    # TO-DO
    for i in range(elements):
        if len(arrA) == 0:
            # appending to the right
            merged_arr += arrB
            break
        elif len(arrB) == 0:
            # appending to the left
            merged_arr += arrA
            break
        elif arrA[0] > arrB[0]:
            merged_arr.append(arrB.pop(0))
        else:
            merged_arr.append(arrA.pop(0))

    return merged_arr


l1 = [2, 3, 4]
l2 = [6, 7, 8]

print(merge(l1, l2))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    print(f"Initial Array is: {arr}")
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr[0:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        # Merge sorted pieces together
        arr = merge(left, right)

    return arr


test = [3, 6, 7, 2, 6, 1, 8, 4, 5, 3]
print(merge_sort(test))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
