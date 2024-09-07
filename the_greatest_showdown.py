# Task 1: Identify the Greatest 
# Write a Python program that asks the user to enter three numbers. 
# Your code should then identify and print out the largest number among the three.

#Task 2: Identify the Smallest 
# Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

# Expected Outcome: If we provide the numbers 3, 3, and 4, 
# it should print out that "The smallest number is 3. The largest number is 4. "

# First, we get our inputs from the user: three integers
x, y, z = int(input("Input x: ")), int(input("Input y: ")), int(input("Input z: "))

# If x is the largest, we declare it so and
if x > y and x > z: 
    largest = x
    # then compare y and z and declare the smallest.
    if y > z: 
        smallest = z
    else: smallest = y
# If y is the largest, we declare it so and
elif y > x and y > z: 
    largest = y
    # then compare x and z and declare the smallest.
    if x > z: 
        smallest = z
    else: smallest = x
# If z is the largest, we declare it so and 
else: 
    largest = z
    # then compare x and y and declare the smallest.
    if x > y: 
        smallest = y
    else: smallest = x

# Print which number is the smallest and which is the largest.
print("The smallest number is " + str(smallest) + ". The largest number is " + str(largest))
    
    