# Write a program to calculate the sum of series up to n term. For example, 
# if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

# Given:
# n = 5

# Expected output:
# 24690

num = int(input("Enter a number: "))
total = 0
number = 2

for i in range(num):
    total = total + number
    number = number * 10 + 2
print(total) 
