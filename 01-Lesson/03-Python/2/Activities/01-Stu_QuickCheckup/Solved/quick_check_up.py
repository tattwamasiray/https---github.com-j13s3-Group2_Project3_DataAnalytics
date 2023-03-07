# Print Hello User!
print("Hello User!")

# Take in User Input
name = input("What is your name? ")

# Respond Back with User Input
print("Hi " + name + "!")

# Take in the User Favourite Number
fave_number = input("What is your favourite number? ")

# Respond Back with a statement based on your favourite number
if (int(fave_number) < 7):
    print("Your favourite number is lower than mine.")

if (int(fave_number) == 7):
    print("Your favourite number is the same as mine!")

if (int(fave_number) > 7):
    print("Your favourite number is higher than mine.")
