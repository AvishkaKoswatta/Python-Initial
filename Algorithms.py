#Sorting Algorithms

# Buble sort
# compares adjacent elements and swaps them
# def bubble_sort(arr):
#     n=len(arr)
#     for i in range (n):
#         for j in range (n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1], arr[j]
    
#     return arr

# print(bubble_sort([1,8,4,3,9,0,12,7]))



# Selection sort
# select the first element of array as minimum and compare with next value first.
# if it is smaller, now the minimum is this value. if not do nothing compare with next
# at end of this i iteration swap final minimum with arr[i]
# repeat process with next minimum as arr[i]

# def selection_sort(arr):
#     n=len(arr)
#     for i in range (n):
#         min_idx = i
#         for j in range (i+1,n):
#             if arr[min_idx] > arr[j]:
#                 min_idx=j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# print(selection_sort([1,4,2,-9,34,9,12]))


# Insertion sort
# first element is consider as an already sorted array. second element is key. compare sorted array with key.
# if key is smaller, move first element to right and place key in the correct place.
# 
# def insertion_sort(arr):
#     n=len(arr)








 # Merge sort
 # divide array into 2 arrays. seperate until isolate one element.
 # connect them while sorting.
 # 
 # 
 # 
 # 
 # 
 # 
 #    



 # Quick sort
 # Picks a pivot element, partitions the list into elements less than and greater than the pivot, 
 # recursively sorts the partitions.

