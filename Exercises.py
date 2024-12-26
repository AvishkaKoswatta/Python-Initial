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



