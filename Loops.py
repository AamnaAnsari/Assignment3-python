# Lesson 05 , 06 , 07 

# 1. The if Statement
# The if statement is used to execute a block of code only if a condition is True.

number: int = 20

if number > 10:
    print("The number is positive")

# 2. The else Statement
# The else statement is used to execute a block of code if the condition is False.

number: int = 4

if number > 10:
    print("The number is positive")
else:
    print("The number is negative")


# 3. The elif Statement
# The elif statement is used to check multiple conditions. It stands for "else if".

number: int = 6

if number > 10:
    print("The number is positive")
elif number < 10:
    print("The number is negative")
else:
    print("The number is zero")

# 4. Nested if Statements
# if statements can be nested inside other if statements to check multiple conditions.

number: int = 20

if number > 10:
    print("The number is positive")
    if number < 20:
        print("The number is less than 20")
else:
    print("The number is negative")

# 5. For Loop
# The for loop is used to iterate over a sequence (list, tuple, string, etc.)

numbers: list[int] = [1, 2, 3, 4, 5,6,7,8,9,10]

for number in numbers:
    print(number)
    

    numbers = [1, 2, 3, 4, 5,6,7]

# Searching with else
for num in numbers:
    if num == 7:
        print("Number found!")
        break
else:
    print("Number not found!")  # Runs because 6 is not in the list

#    6. Controlling Loops
# Python provides two keywords (break & continue) to control loops:

# break: Exits the loop immediately.
# continue: Skips the rest of the code in the current iteration and moves to the next iteration.

numbers: list[int] = [1, 2, 3, 4, 5,6,7,8,9,10]

for num in numbers:
    if num == 6:
        break
    print(num)

# Continue example
for i in range(8):
    if i == 3:
        continue
    print(i)  # Prints 0, 1, 2, 4

# While Loop Example
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# Nested While Loop Example
outer_count = 0
while outer_count < 3:
    inner_count = 0
    while inner_count < 3:
        print(f"Outer: {outer_count}, Inner: {inner_count}")
        inner_count += 1
    outer_count += 1

# 7. The range() Function
# The range() function generates a sequence of numbers.

# range(stop)
# range(start, stop)
# range(start, stop, step)  

for i in range(2):
    print(i) 

for i in range(4, 6):
    print(i)  

for i in range(8, 10, 12):
    print(i) 


# 08: Lists, Tuples & Dictionary

# List Example
fruits = ["Apple", "Banana", "Cherry","Mango", "cherry"]
fruits.append("orange")  # Adding an element
print("Fruits List:", fruits)

# Tuple Example
days = ("Monday", "Tuesday", "Wednesday")
print("Tuple Example:", days[0])  

# Dictionary Example
student = {"name": "Ali", "age": 20, "grade": "A"}
student["city"] = "Karachi"  
print("Student Dictionary:", student)

# 09: The Set & Frozenset

# Set Example
numbers = {1, 2, 3, 4, 5}
numbers.add(6)  # Adding an element
print("Set Example:", numbers)

#10: # Frozenset Example

immutable_set = frozenset([10, 20, 30, 40])
print("Frozenset Example:", immutable_set)



