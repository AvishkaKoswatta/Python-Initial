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

#list comprehension
fruits=["apple","orange","kiwi"]
new_friuts=[]
for y in fruits:
    if "a" in y:
        new_friuts.append(y)

print(new_friuts)

#................................above same as below 
new_friuts=[y for y in fruits if "a" in y]

#Sort List
#alphanumerically, ascending, by default
thislist=["a","c","de"]
thislist.sort()
thislist.sort(reverse=True)

#Reverse Order
thislist.reverse()

#Copy of a list
#list1=list2 is making changes in one list to other list
copylist=thislist.copy()
copylist=list(thislist)
copylist=thislist[:] #slice operater


#Join Two Lists
listnew=["a","b","c"]
listold=[1,2,3]

joinlist=listnew + listold

for x in listold:
    listnew.append(x)

listold.extend(listnew)

# Method 	    Description
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list



#TUPLE

#Ordered , unchangeable , indexed , allow duplicates

mytuple=("a", "e", 1 , True)

#access
print(mytuple[1])

#Tupples can not add, remove and change. but,
#To update a tupple once it has created,
#convert the tuple into a list, change the list, and convert the list back into a tuple.

tuplelist=list(mytuple)
#any list method operation
mytuple=tuple(tuplelist)

#creating a tuple with only one item, include a comma after the item
oneitemtuple=("kiwi",)

#delete completely
del mytuple

#Join Two Tuples
tuple1=(1,2,3)
tuple2=(4,5)
tuple3=tuple1+tuple2



#SETS
#unordered, unchangeable* but can add or remove, unindexed , no duplicates allow
myset={"a","b",1}

#Access set items
#if "a" present in the set, use in keyword
print("a" in myset)

#Add Set Items
myset.add("c")

#add items from another set
thisset=("g","h")
myset.update(thisset) #second items do not have to be a set

#Remove Set Items
myset.remove("a")
myset.discard("b")
myset.pop() #remove random item

#delete entire set
del myset

#Join Sets

set1=("a","b","c",1)
set2=(1,2,3,4)

#union() and update() - joins all items from both sets
set3 = set1.union(set2)
set3 = set1 | set2
set3 = set1.update(set2)
set3 = set1.union(set2, myset, thisset)
set3 = set1 | set2 | myset | thisset

#intersection() - keeps ONLY the duplicates
set4 = set1.intersection(set2)
set4 = set1 & set2

#difference() - return a new set, only the items from the first set that are not present in the other set
set5 = set1.difference(set2)
set5 = set1 - set2

#symmetric_difference() - keep only the elements that are NOT present in both sets
set6 = set1.symmetric_difference(set2)
set6 = set1 ^ set2