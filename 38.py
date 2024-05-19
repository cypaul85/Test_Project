# 038
# hange program 037 to also ask for a number. Display their name (one letter at a time on each line) 
# and repeat this for the number of times they entered.


name = input("Enter your name? ")
num = int(input("Enter a number that you want to repeat? "))

for i in range(num):
    for c in name:
        print(c)

