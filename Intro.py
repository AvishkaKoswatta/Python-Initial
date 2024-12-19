print("Hello")

# Indentation refers to the spaces at the beginning of a code line
if(5>2):
    print("Five greater than two")

#VARIABLES

#Variables do not need to be declared with any particular type
#Can even change type after they have been set
#Python decides the type automatically
#Variable names are case-sensitive

name="abc"
age=25
height=5.3
is_true=True
print(name,age,height,is_true)

print(type(name))

x="red", "white", "blue"
x=y=z="red"

#DATA TYPES
# x = "Hello World" 	                        str 	
# x = 20 	                                    int 	
# x = 20.5 	                                    float 	
# x = 1j 	                                    complex 	
# x = ["apple", "banana", "cherry"] 	        list 	
# x = ("apple", "banana", "cherry") 	        tuple 	
# x = range(6) 	                                range 	
# x = {"name" : "John", "age" : 36} 	        dict 	
# x = {"apple", "banana", "cherry"} 	        set 	
# x = frozenset({"apple", "banana", "cherry"}) 	frozenset 	
# x = True 	                                    bool 	
# x = b"Hello" 	                                bytes 	
# x = bytearray(5) 	                            bytearray 	
# x = memoryview(bytes(5)) 	                    memoryview 	
# x = None 	                                    NoneType

#Strings
#Strings in Python are arrays
array="Hello"
print(array[1])
print(len(array))

#in
if "world" in array:
    print("Yes")

#not in
if "world" not in array:
    print("world not in array")

#slicing
#return a range of characters
x="hello world"
print(x[1:5]) #include 1. not include 5. only upto 4
print(x[:5])
print(x[3:])
print(x[-6:-2]) #

#Lists
#List items are ordered, changeable, and allow duplicate values.
list=["a","b","c",1,"a"]

#To insert a new list item at a specified index, without replacing any of the existing values, use insert() method.
list1=["a","b",1]
list1.insert(2,"c")

#To add an item to the end of the list, use the append() method
list1.append("d")

#To append elements from another list to the current list use extend() method
list.extend(list1)

#remove item
list1.remove("b")

#remove from specific index
list1.pop(2)