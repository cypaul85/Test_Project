# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
# Given:
# list1 = [100, 200, 300, 400, 500]

# Expected output:
# [500, 400, 300, 200, 100]

list1 = [100, 200, 300, 400, 500]

# rev = list(reversed(list1))
rev = list1[::-1]
print(rev)