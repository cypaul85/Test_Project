# 043
# Ask which direction the user wants to count (up or down). If they select up, then ask
# them for the top number and then count from 1 to that number. If they select down, ask
# them to enter a number below 20 and then count down from 20 to that number. If they
# entered something other than up or down, display the message “I don’t understand”.

answer = input("Enter the directon that you want to count(up or down)")

if answer == "up":
    num = int(input("Enter the top number? "))
    for i in range(1,num+1):
        print(i)
elif answer == "down":
    num = int(input("Enter a number under 20? "))
    for i in range(20, num-1, -1):
        print(i)
else:
    print("I don't understand")