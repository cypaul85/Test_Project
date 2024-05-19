# 047
# Ask the user to enter a number and then enter another number. Add these
# two numbers together and then ask if they want to add another number. If they
# enter “y", ask them to enter another number and keep adding numbers until they
# do not answer “y”. Once the loop has stopped, display the total.

total = num = int(input("Enter a number? "))
answer = "y"

while answer == "y":
    num = int(input("Enter a number? "))
    total = total + num
    answer = input("Do you want to add another number(y or n)? ")

print("The total is", total)