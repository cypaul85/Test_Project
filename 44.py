# 044
# Ask how many people the user wants to invite to a party. If they enter a number below
# 10, ask for the names and after each name display “[name] has been invited”. If they
# enter a number which is 10 or higher, display the message “Too many people”.

num = int(input("How many people do you want to invite to your party? "))

if num >= 10:
    print("Too many people")
else:
    for i in range(num):
        name = input("Enter the name: ")
        print(name,"has been invited.")
