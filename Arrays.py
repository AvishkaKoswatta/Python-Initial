#Python does not have built-in support for Arrays
#Python Lists
#Python has a great built-in list type named "list".
#List is a collection which is ordered and changeable. Allows duplicate members.
#Lists are written with square brackets.
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list.

num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed Number:", reversed_num)
