# Use a loop to display elements from a given list present at odd index positions
# Given
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Expected
# 20 40 60 80 100

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

length = len(my_list)

for i in range(length):
    if i % 2 == 1:
        print(my_list[i], end=" ")
        