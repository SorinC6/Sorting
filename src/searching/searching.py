# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for i in range(0, len(arr)):
        if target == arr[i]:
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    first = 0
    last = len(arr)-1

    while first <= last:
        middle = int((first+last) / 2)

        if(arr[middle] == target):
            return middle
        else:
            if target < arr[middle]:
                last = middle-1
            else:
                first = middle+1

    return -1


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls

    middle = (low+high) // 2

    if(arr[middle] == target):
        return middle
    elif target < arr[middle]:
        return binary_search_recursive(arr, target, low, high-1)
    else:
        return binary_search_recursive(arr, target, low + 1, high)
