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