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