#execute a set of statements as long as a condition is true
#while loop runs as long as, or while, a certain condition is true

i=1
while i<5:
    i+=1
    print(i)


#break
#stop the loop even if the while condition is true
i=1
while i<8:
   print(i)
   if i==5:
      break
   i+=1   
#1,2,3,4,5


#continue
#stop the current iteration, and continue with the next
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  #1,2,4,5,6



prompt="Tell me anything: "
message=""
while message != "quite":
   message=input(prompt)
   print(message)
   if message=="quite":
      print("Bye")


#using a flag when there is more conditions to quit
flag=1
while flag:
   message=input("Enter: ")
   if message=="quit":
      flag=0
   else:
      print(message) 


#enter infinite inputs until quit
while True:
   message=input("Enter grocery list: ")
   if message=="done":
      break
   else:
      print(message)


#print only even numbers.
number=0
while number<10:
   number+=1
   if number % 2 == 1:
      continue
   print(number) 


#loop for check age and display ticket price
print("Movie Ticket")
while True:
   age=int(input("Enter your age: "))
   if age<3:
      print("Free")
   elif 3<age<=12:
      print("$10")
   else:
      print("$15")
      
   break


#for loop is effective for looping through a list
#shouldn’t modify a list inside a for loop 
#To modify a list use while loop
