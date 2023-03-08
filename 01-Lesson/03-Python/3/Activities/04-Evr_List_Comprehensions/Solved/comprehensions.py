fish = "halibut"

# Loop through each letter in the string
# and push to an array
letters = []
for letter in fish:
    letters.append(letter)

print(letters)

# List comprehensions provide concise syntax for creating lists
letters = [letter for letter in fish]

print(letters)

# We can manipulate each element as we go
capital_letters = []
for letter in fish:
    capital_letters.append(letter.upper())

print(capital_letters)

# List Comprehension for the above
capital_letters = [letter.upper() for letter in fish]

print(capital_letters)

# We can also add conditional logic (if statements) to a list comprehension
jan_temperatures = [30, 29, 33, 26, 41]
hot_days = []
for temperature in jan_temperatures:
    if temperature > 32:
        hot_days.append(temperature)
print(hot_days)

# List Comprehension with conditional
hot_days = [temperature for temperature in jan_temperatures if temperature > 32]

print(hot_days)
