# Calculate the sum of all numbers from 1 to a given number

num = int(input("Enter a number: "))
total = 0

for i in range(1, num + 1):
    total = total + i
print("The total is", total)