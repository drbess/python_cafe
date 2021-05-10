# program to illustrate explicit type conversion
# creating addition() function to add two numbers
def addition(a, b):


print("Type of first number(a) :", a, type(a))
print("Type of second number(b) :", b, type(b))

c = a + b

print("Type of resulting variable(c) :", c, type(c))
# addition() function calls with different inputs
print("accepting input from the user -->")
print("Enter first number")
# Explicit type casting
num1 = int(input())
print("Enter second number")
num2 = int(input())
# addition() function call
addition(num1, num2)
print('\n')