import os
import csv

work_csv = os.path.join("..", "Resources", "Absenteeism_at_work.csv")

# Lists to store data
reason_for_absence = []
distance_from_work = []
service_time = []
age = []
hit_target = []
absenteeism_time_in_hours = []
percentage_of_day_missed  = []

# with open(work_csv, encoding='utf-8') as csvfile:
with open(work_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add reason for absence
        reason_for_absence.append(row[1])

        # Add distance from work
        distance_from_work.append(row[6])

        # Add service time
        service_time.append(row[7])

        # Add age
        age.append(row[8])

        # Determine percentage of day missed, given an eight hour work day
        percent = round(int(float(row[20])) / 8 * 100, 2)
        percentage_of_day_missed.append(str(percent) + "%")

        # Add absenteeism time in hours
        absenteeism_time_in_hours.append(row[20])
        

# Zip lists together
cleaned_csv = zip(reason_for_absence, distance_from_work, service_time, age, percentage_of_day_missed, absenteeism_time_in_hours)

# Set variable for output file
output_file = os.path.join("absenteeism_final.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Reason for Absence", "Distance from Work", "Service Time", "Age", "Percentage of Day Missed", "Absenteeism Time in Hours"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
