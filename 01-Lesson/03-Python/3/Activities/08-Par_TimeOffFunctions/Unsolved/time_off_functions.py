import os
import csv

# Path to collect data from the Resources folder


# Define the function and have it accept the 'employee_data' as its sole parameter


# Find the total allowed time off

# Find the total taken time off

# Find the rate of use for PTO

# Remember that some employees do not have sick time
# Find the sick time usage rate

# Find the voting time usage rate

# Calculate the overall time off usage rate

# Print out the employee's id and usage rate stats


# Read in the CSV file
with open(pto_hours_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what employee_id they would like to search for
    employee_id_to_check = input("Which employee_id do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the employee_id is in a row is equal to that which the user input, run the 'print_percentages()' function
        if employee_id_to_check == row[0]:
            print_percentages(row)
