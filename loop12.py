# Find the factorial of a given number

num = int(input("Enter a number: "))
total = 1

for i in range(num, 0, -1):
    total = total * i
print(total)