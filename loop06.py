# Write a program to count the total number of digits in a number using a while loop.

# For example, the number is 75869, so the output should be 5.

num = 758698
count = 0

while num > 0:
    num = num // 10
    count = count + 1
print(count)