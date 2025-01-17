#Sorting Algorithms
# Buble sort
# compares adjacent elements and swaps them
def bubble_sort(arr):
    n=len(arr)
    for i in range (n):
        for j in range (n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1], arr[j]
    
    return arr

print(bubble_sort([1,8,4,3,9,0,12,7]))

