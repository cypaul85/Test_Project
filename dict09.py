# Exercise 9: Get the key of a minimum value from the following dictionary

# Given dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

# Expected output:
# Math

print(min(sample_dict, key=sample_dict.get))