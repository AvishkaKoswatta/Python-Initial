#Slicing in python
#Slicing is a way to extract a subsequence from a sequence in python.
#Slicing can be applied to any sequence like list, string, tuple etc.
#Syntax:
#sequence[start:stop:step]
#start: starting index of the sequence
#stop: ending index of the sequence
#step: step size of the sequence
#Note: The stop index is not included in the output.

#Example:

list1=[1,2,3,4,5,6,7,8,9,10]

#list1[2:5]     will return [3,4,5]
#list1[2:5:2]   will return [3,5]
#list1[::2]     will return [1,3,5,7,9]
#list1[::-1]    will return [10,9,8,7,6,5,4,3,2,1]
#list1[5:2:-1]  will return [6,5,4]
#list1[5:2:-2]  will return [6,4]
#list1[5:2:1]   will return []
#list1[2:5:-1]  will return []
