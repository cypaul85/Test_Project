# 048
# Ask for the name of somebody the user wants to invite to a party. 
# After this, display the message “[name] has
# now been invited” and add 1 to the count. Then ask if
# they want to invite somebody else. Keep repeating this
# until they no longer want to invite anyone else to the
# party and then display how many people they have
# coming to the party.

again = "y"
count = 0

while again == "y":
    name = input("Enter a name you want to invite to a party? ")
    print(name, "has now been invited.")
    count = count + 1
    again = input("Do you want to invite another person(y or n)? ")

print(count, "people have been invited.")