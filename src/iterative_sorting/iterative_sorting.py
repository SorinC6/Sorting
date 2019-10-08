# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        min_position = i

        # TO-DO: find next smallest element
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_position]:
                min_position = j

        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[min_position]
        arr[min_position] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
# def bubble_sort(arr):

#     for i in range(0, len(arr)-1):
#         for j in range(0, len(arr)-1-i):
#             if(arr[j] > arr[j+1]):
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp

#     return arr


# Using While
def bubble_sort(arr):

    isSorted = True
    while isSorted:
        isSorted = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                isSorted = True

    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
