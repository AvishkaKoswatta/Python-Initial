# 1. Basic while Loop

# A while loop executes as long as the condition remains true.
# Example:

i = 1
while i < 5:
    i += 1  # Increment i in each iteration
    print(i)

# Explanation:
#     Starts with i = 1.
#     The loop runs as long as i < 5.
#     Increments i by 1 in each iteration and prints it.
#     Output: 2, 3, 4, 5.


# 2. break Statement
# The break statement exits the loop immediately, even if the loop condition is still true.
# Example:

i = 1
while i < 8:
    print(i)
    if i == 5:  # Exit the loop when i equals 5
        break
    i += 1
# Output: 1, 2, 3, 4, 5.


# 3. continue Statement
# The continue statement skips the current iteration and moves to the next.
# Example:

i = 0
while i < 6:
    i += 1
    if i == 3:  # Skip printing when i equals 3
        continue
    print(i)
# Output: 1, 2, 4, 5, 6.


# 4. Input with while Loop
# Repeats until a specific condition is met.
# Example:

prompt = "Tell me anything: "
message = ""
while message != "quite":  # Keep looping until "quite" is entered
    message = input(prompt)
    print(message)
    if message == "quite":
        print("Bye")

# Behavior:

#     The loop asks for input until the user types quite.
#     Example Output:
#     Tell me anything: Hello
#     Hello
#     Tell me anything: quite
#     Bye



# 5. Using a Flag for Multiple Conditions
# A flag controls when to stop the loop, especially if there are multiple exit conditions.
# Example:

flag = 1
while flag:  # The loop runs as long as the flag is true (non-zero)
    message = input("Enter: ")
    if message == "quit":  # Condition to exit the loop
        flag = 0
    else:
        print(message)



# 6. Infinite Inputs Until "done"
# Using while True to run an infinite loop until a condition breaks it.
# Example:

while True:
    message = input("Enter grocery list: ")
    if message == "done":  # Stop when "done" is entered
        break
    else:
        print(message)



# 7. Print Only Even Numbers
# Skip odd numbers using the continue statement.
# Example:

number = 0
while number < 10:
    number += 1
    if number % 2 == 1:  # Skip odd numbers
        continue
    print(number)
# Output: 2, 4, 6, 8, 10.


# 8. Age-Based Movie Ticket Prices
# Check age and display appropriate ticket prices.
# Example:

print("Movie Ticket")
while True:
    age = int(input("Enter your age: "))
    if age < 3:
        print("Free")
    elif 3 <= age <= 12:  
        print("$10")
    else:
        print("$15")
    break


# 9. Modify a List Using while
# Use a while loop to move items between lists.
# Example:

order = ["apple", "banana", "orange"]
delivered = []

# Move items from `order` to `delivered`
while order:
    i = order.pop()  # Remove the last item from `order`
    delivered.append(i)  # Add it to `delivered`

# Print the items in `delivered`
for j in delivered:
    print(j.title())

print(delivered)  # Final state of `delivered`

# Output:

# Orange
# Banana
# Apple
# ['orange', 'banana', 'apple']



# Key Notes:

#     Use while for Indeterminate Loops:
#         When the number of iterations is not fixed.
#         Example: Reading user input until a condition is met.

#     Avoid Infinite Loops:
#         Ensure there’s a condition to break out of the loop.
#         Example: Use break or update loop variables.

#     Avoid Modifying Lists in for Loops:
#         Use while to modify lists dynamically