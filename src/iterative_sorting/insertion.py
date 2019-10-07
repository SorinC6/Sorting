def insertion_sort(arr):
    # separate the first element from the rest of the array (a sorted list of 1 element for now)
    # begin with the second element
    for i in range(1, len(arr)):
        # copy the first element in a variable
        temp = arr[i]  # first one

        j = i
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    return arr


l = insertion_sort([4, 3, 6, 1])
print(l)


#  ================First========
# array=[4,3,6,1]
# > [4,   3,6,1]

# temp=3
# j=1
#     while i>0 and 3 < 4:
#         arr[j]=4   [4,4,6,1]
#         j=0
#     arr[0]=3       [3,4,6,1]
# >

#  ================Second========
#  array = [3,4,6,1]
#  temp=6
#  j=2
# while j>0 and 6 < 3
#     break;

#  ================Second========
#  array = [3,41,6,]
#  temp=1
#  j=3
#  while j>0 and 1<6
#     arr[3]=6   [3,4,6,6]
#     j=2
# list[2] = 1    [3,4,1,6] > [3,1,4,6]  > [1,3,4,6]  !
