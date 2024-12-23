def greeting(name):
   print(f"Hello, {name.title()}")

greeting("Anne")

#Argument
#Information passed from function call to function- "Anne"

#Parameter
#Information the function need to do the job- name

def shirts(size,text):
   print(f"This shirt size is {size} and {text} should be printed")

shirts(size="xl",text="Hello, World")
shirts("xxl","Hi")

#dictionary
def full_name(first,last):
   dict={'first_name':first,'last_name':last}
   return dict

print('Anne', 'Marry')

#lists
def greet_list():
   for name in names:
    print(f"Hello, {name}")

names=["Anne", "Marry", "John"]
greet_list()
