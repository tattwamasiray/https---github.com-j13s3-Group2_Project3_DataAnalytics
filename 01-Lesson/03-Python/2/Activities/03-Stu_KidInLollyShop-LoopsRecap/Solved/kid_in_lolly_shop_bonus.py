# The list of lollies to print to the screen
lolly_list = [
    "Fantales", 
    "Snakes Alive", 
    "Minties", 
    "Liquorice Allsorts", 
    "Strawberries & Cream", 
    "Life Savers", 
    "Banana Lollies", 
    "Fruit Pastilles", 
    "Sherbies"
]

# The list used to store all of the lollies selected inside of
lolly_cart = []

# Print all of the candies to the screen and their index in brackets
for i in range(len(lolly_list)):
    print("[" + str(i) + "] " + lolly_list[i])


# Set answer to "yes" for while loop
answer = "yes"


while answer == "yes":

    # Ask which lolly the user would like to bring home
    print("Which lolly would you like to bring home?")
    selected = input("Input the number of the lolly you want: ")

    # Add the lolly at the index chosen to the lolly_cart list
    lolly_cart.append(lolly_list[int(selected)])

    # ask the user if they want more candy
    answer = input("Would you like to make another selection? ('yes' or 'no') ")


# Loop through the lolly_cart to say what lollies were brought home
print("I brought home with me...")
for lolly in lolly_cart:
    print(lolly)
