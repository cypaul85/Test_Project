# Write a program to print multiplication table of a given number

num = int(input("Enter a number: "))

for i in range(1, 10):
    print(num, "*", i, "=", num * i)
    