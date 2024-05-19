# Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables 
# and calculate addition and subtraction. Also, it must return both addition and subtraction 
# in a single return call.
# calculation(40, 10)

def calculation(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    return add, sub

res = calculation(40, 10)
print(res)