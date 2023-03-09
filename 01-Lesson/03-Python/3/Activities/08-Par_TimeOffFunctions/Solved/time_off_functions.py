import os
import csv

# Path to collect data from the Resources folder
pto_hours_csv = os.path.join('..', 'Resources', 'pto_hours.csv')


# Define the function and have it accept the 'employee_data' as its sole parameter
def print_percentages(employee_data):
    # For readability, it can help to assign your values to variables with descriptive names
    # CSV headers: Employee ID, PTO Hours (Allowed), PTO Hours (Taken), Sick Hours (Allowed),
    #  Sick Hours (Taken), Voting Time (Allowed), Voting Time (Taken)
    employee_id = str(employee_data[0])
    pto_hours_allowed = int(employee_data[1])
    pto_hours_taken = int(employee_data[2])
    sick_hours_allowed = int(employee_data[3])
    sick_hours_taken = int(employee_data[4])
    voting_time_allowed = int(employee_data[5])
    voting_time_taken = int(employee_data[6])

    # Total number of allowed time off days can be found by adding each category together
    total_allowed = pto_hours_allowed + sick_hours_allowed + voting_time_allowed
    # Total number of taken time off days can be found by adding each category together
    total_taken = pto_hours_taken + sick_hours_taken + voting_time_taken

    # Calculating the rate of use for PTO can be calculated by doing the following
    pto_rate = (pto_hours_taken / pto_hours_allowed) * 100

    # Note that some employees do not have sick time, so we will need to account for potential 0 sick time.

    # Sick hour usage rate can be calculated by doing the following
    if sick_hours_allowed == 0:
        sick_hours_rate = 0
    else:
        sick_hours_rate = (sick_hours_taken / sick_hours_allowed) * 100

    # Calculate voting time usage rate by doing the following
    voting_time_usage_rate = (voting_time_taken / voting_time_allowed) * 100

    # Calculate the overall time off usage
    overall_usage_rate = (total_taken / total_allowed) * 100

    # If the overall time off usage is greater than 50%, note Adequate Time Off
    # Otherwise it is "Encourage employee to take time off".
    if overall_usage_rate > 50:
        message = "Adequate Time Off"
    else:
        message = "Encourage employee to take time off"

    # Print out the employee's id and their time off usage rates.
    print(f"Stats for {employee_id}")
    print(f"PTO Usage Rate: {str(pto_rate)}")
    print(f"Sick Time Usage Rate: {str(sick_hours_rate)}")
    print(f"Voting Time Usage Rate: {str(voting_time_usage_rate)}")
    print(f"Overall Time Off Usage: {str(overall_usage_rate)}")
    print(f"{message}")


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
