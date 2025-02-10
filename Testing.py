# x="helloworld"
# #print(x[1:5])  
# print(x[:-1])
# # print(x[3:])
# # print(x[-6:-2]) 


# def maximum_value():
#     # Read K and M
#     K, M = map(int, input().split())  # Convert input to integers
#     y = []  # List to store squared max values
    
#     # Read K lists
#     for _ in range(K):
#         lst = list(map(int, input().split()[1:]))  # Read list and ignore the first element
#         y.append(max(lst) ** 2)  # Square the max value and add to y
    
#     # Compute and return the result
#     return sum(y) % M

# # Call function and print result
# print(maximum_value())



# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
# int list A
# int list B
# print the cartesian product of A and B


# A=list(input())
# B=list(input())

# print(list(product(A, B)))

#print(*product(A, B))





# print fibonacci in python
def fibonacci(n):
    a,b=0,1
    f=[]
    for i in range(n):
        f.append(a)
        a,b=b,a+b
    print(f)

fibonacci(10)