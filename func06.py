# Create a recursive function
# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# A recursive function is a function that calls itself again and again.

# Expected Output:
# 55

def add(n):
    if n > 1:
        return n + add(n-1)
    return n

res = add(100)
print(res)