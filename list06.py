# Exercise 6: Remove empty strings from the list of strings

# Given
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Expected output:
# ["Mike", "Emma", "Kelly", "Brad"]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)