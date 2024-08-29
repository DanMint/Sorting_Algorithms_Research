# Data
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = ["a", "b", "c"]

# Create dictionary
c = {key: [row[i] for row in a] for i, key in enumerate(b)}

# Output the dictionary
print(c)
