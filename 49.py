# 049
# Create a variable called compnum and set the value
# to 50. Ask the user to enter a number. While their guess
# is not the same as the compnum value, tell them if
# their guess is too low or too high and ask them to have
# another guess. If they enter the same value as
# compnum, display the message “Well done, you
# took [count] attempts”.

compnum = 50
count = 0
num = 0

while compnum != num:
    num = int(input("Guess the number? "))
    if num > compnum:
        print("Too high")
    elif num < compnum:
        print("Too low")
    count = count + 1

print("Well done, you took", count, "attempts.")