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
def selection_sort(arr):
    n=len(arr)
    for i in range (n):
        min_idx = i
        for j in range (i+1,n):
            if arr[min_idx] > arr[j]:
                min_idx=j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([1,4,2,-9,34,9,12]))