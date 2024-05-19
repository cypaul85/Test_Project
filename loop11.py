#  Display Fibonacci series up to 10 terms

# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34
num1, num2 = 0, 1
print(num1, num2, end=" ")

for i in range(8):
    num3 = num1 + num2
    print(num3, end=" ")
    num1 = num2
    num2 = num3
print()