# Reverse a given integer number
# Given:
# 76542

# Expected output:
# 24567

number = 76542
new_Num = 0

while number > 0:
    remain = number % 10
    number = number // 10
    new_Num = new_Num * 10 + remain

print(new_Num)