radius=input("Enter the radius of the circle: ")
radius=float(radius)
area=3.14159*radius**2
print("Area of the circle: ", area)

number=12
if number%2==0:
    print("The number is even")
else:
    print("The number is odd")


i = 1
sum=0
while i<4:
    sum+=i
    i=i+1

print(sum)


fact=1
for i in range(1,4):
    fact=fact*i

print(fact)




first=0
second=1
i=0
while i<=20:
    print(first)
    next=first+second
    first=second
    second=next
    i=i+1



num=12345
reversed_num=0
while num>0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num=num//10

print("Reversed Number is: ",reversed_num)



#Create a list
numbers=input("Enter a number: ")
numbers=int(numbers)
num_list=[]
i=0
while i<numbers:
    num=input("Enter numbers:")
    num_list.append(num)
    i+=1

print(num_list)



#swapp 2 numbers
num=0
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))

print("num1= ",num1)
print("num2= ",num2)

num=num1
num1=num2
num2=num

print("After swapping")
print("num1= ",num1)
print("num2= ",num2)




#reverse a number
num1=int(input("Enter a number: "))
x=0

while num1>0:
    digit=num1%10
    x=x*10+digit
    num1=num1//10

print("Reversed Number is: ",x)





#Add the numbers in a user input integer.
def total():
    temp=0
    number=int((input("Enter a number: ")))
    while number>0:
        digit=number%10
        temp=temp+digit
        number=number//10
    print("Total is: ",temp)

total()



#Reverse a string
def reverse_string():
    string1 = input("Enter a string: ")   
    reversed_string = ""  
    
    for i in range(len(string1) - 1, -1, -1): #start from the last character. go upto the first character. step -1
        reversed_string += string1[i]
    
    print("Reversed String:", reversed_string)

reverse_string()




#Count the number of digits and non-digit characters in a string.
def counting():
    count_digits = 0
    count_others = 0

    str1 = input("Enter the string: ")

    for char in str1:
        if '0' <= char <= '9':  
            count_digits += 1
        else:
            count_others += 1 

    print("Number of digits:", count_digits)
    print("Number of non-digit characters:", count_others)

counting()




#Count the number of vowels in a string.
def count_vowels():
    count=0
    str1=str((input("Enter a string: ")))
    lowercase=str1.lower()
    for char in lowercase:
        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
            count+=1
    print("Number of vowels: ",count)

count_vowels()



#Check if a number is binary or not.
def isBinary():
    flag=0
    num=int((input("Enter a number: ")))
    while num>0:
        digit=num%10
        if digit==0 or digit==1:
            flag=1
        else:
            flag=0
            break
        num=num//10
    if flag==1:
        print("The number is binary")
    else:
        print("The number is not binary")


isBinary()



#Sum of series 1+1/2+1/3+1/4+1/5+...+1/n
def sum_seies():
    n=int(input("Enter the number of terms: "))
    sum=float(0)
    i=1
    while i<=n:
        sum+=1.0/i #floating point division
        i+=1
    print("Sum of series is: ",sum)

sum_seies()



# Minimum and maximum values in a list
def list_min_max():
    mylist=[1,2,3,4,5,6,7,8,9,10]
    print("Minimum value: ",min(mylist))
    print("Maximum value: ",max(mylist))
    print("Sum of the list: ",sum(mylist))

list_min_max()



# Convert binary to decimal
def binary_to_decimal():
    binary=int(input("Enter a binary number: "))
    i=0
    decimal=0

    while binary>0:
        digit=binary%10
        decimal=decimal+(digit*pow(2,i))
        binary=binary//10
        i+=1

    print("Decimal Number is: ",decimal)

binary_to_decimal()




# Convert decimal to binary
def decimal_to_binary():
    decimal=int(input("Enter a decimal number: "))
    binary=""
    i=0
    reversed_string = "" 
    while decimal>0:
        remainder=decimal%2
        decimal=decimal//2
        binary+=str(remainder)
    
    for i in range(len(binary) - 1, -1, -1): 
        reversed_string += binary[i]
    
    print("Reversed String:", reversed_string)

decimal_to_binary()






def is_leap(year):
    leap = False
    
     
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap=True
            else:
                leap=False
        else:
            leap=True
        
    
    return leap

year = int(input())
print(is_leap(year))






def merge_the_tools():
    string, k = input(), int(input())
    for i in range (0,len(string),k):
        t=set(string[i:k])
        result="".join(sorted(t))
        print(result)
        k=k+k

merge_the_tools()
# aasdfg
# 3
# as
# dfg