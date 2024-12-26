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