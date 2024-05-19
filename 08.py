# Ask for the total price of the bill, then ask how many diners there are. 
# Divide the total bill by the number of diners and show how much each person must pay.

price = int(input("Enter the total price of bill? "))
people = int(input("Enter how many diners are? "))

amount = price / people
print("The amount that each person has to pay is $", amount)