# Task 1: Code Correction 
# You are provided with a Python script that uses conditional statements 
# to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

# Error because input takes a string, so we needed to convert it to an int or float
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
# Error because there was only one equal sign. 
elif number == 0:
    print("The number is zero.")
# Error because the else statement gave a condition
else:
    print("The number is negative.")