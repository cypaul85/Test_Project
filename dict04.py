# Exercise 4: Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.

# Given:
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# Expected output:
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res_dict = dict()

for item in employees:
    res_dict.update({item:defaults})

print(res_dict)