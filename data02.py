# Exercise 2: Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position 
# and at the end of the list

# Given:
# list1 = [34, 54, 67, 89, 11, 43, 94]

# Expected Output:

# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]

list1 = [34, 54, 67, 89, 11, 43, 94]

item = list1.pop(4)
print(list1)

list1.insert(2, item)
print(list1)

list1.append(item)
print(list1)