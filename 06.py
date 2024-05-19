# Ask how many slices of pizza the user started with and ask how many slices they have eaten.
# Work out how many slices they have left and display the answer in a userfriendly format.

num1 = int(input("Do you remember how pieces of pizza were available? "))
num2 = int(input("How many pieces of pizza did you eat? "))
answer = num1 - num2
print("There are", answer,"pieces of pizza still remained.")