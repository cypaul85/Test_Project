# Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of arguments and print their value.

# Given
# func1(20, 40, 60)
# func1(80, 100)

# Expected Output:
# Printing values
# 20
# 40
# 60

# Printing values
# 80
# 100

def func1(*args):
    print("Printing Values")
    for i in args:
        print(i)
print()

func1(20, 40, 60)
func1(80, 100)