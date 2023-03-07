# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Pie List
pie_list = ["Aussie Beef", "Steak and Kidney", "Chicken", "Shepherd's", "Spinach and Feta", 
            "Curry", "Lamb and Rosemary", "Steak and Mushroom", "Apple", "Lemon Meringue"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while shopping == "y":

    # Show pie selection prompt
    print("---------------------------------------------------------------------")
    print("(1) Aussie Beef, (2) Steak and Kidney, (3) Chicken, (4) Shepherd’s, " +
          "(5) Spinach and Feta, (6) Curry, (7) Lamb and Rosemary, (8) Steak and Mushroom, " +
          "(9) Apple, (10) Lemon Meringue")

    pie_choice = input("Which would you like? ")

    # Get index of the pie from the selected number
    choice_index = int(pie_choice) - 1

    # Add pie to the pie list by finding the matching index and adding one to its value
    pie_purchases[choice_index] += 1

    print("------------------------------------------------------------------------")

    # Inform the customer of the pie purchase
    print("Great! We'll have that " + pie_list[choice_index] + " right out for you.")

    # Provide exit option
    shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

# Once the pie list is complete
print("------------------------------------------------------------------------")

# Count instances of each pie
print("You purchased: ")

# Loop through the full pie list
for pie_index in range(len(pie_list)):
    pie_count = str(pie_purchases[pie_index])
    pie_name = str(pie_list[pie_index])

    # Gather the count of each pie in the pie list and print them alongside the pies
    print(pie_count + " " + pie_name)
