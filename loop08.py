# Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]

# Expected output:

# 50
# 40
# 30
# 20
# 10

list1 = [10, 20, 30, 40, 50]

size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])