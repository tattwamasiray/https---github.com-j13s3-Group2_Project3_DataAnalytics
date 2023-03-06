# Absenteeism at Work

In this activity, you will be provided with a large dataset with Absenteeism from Work data. Your task is to clean up this dataset and create a new CSV file that is easier to comprehend.

## Instructions

* Create a Python application that reads in the data.

* Store the contents of `Reason for Absence`, `Distance From Work`, `Service Time`, `Age`, and `Absenteeism Time in Hours` in Python Lists.

* Zip these lists together into a single tuple.

* Write the contents of your extracted data into a CSV. Make sure to include the titles of these columns in your CSV.

## Bonus

* Find the percentage of work missed given an 8-hour work day. Include this in your final output, converting the rate to a string and including a "%" at the end of the string.

## Hints

* Windows users may get a `UnicodeDecodeError`. To avoid this, pass in `encoding="utf8"` as an additional parameter when reading in the file.

* As with many datasets, the file does not include the header line. Use the following list as a guide to the columns: "ID, Reason for absence, Month of absence, Day of the week, Seasons, Transportation expense, Distance from Residence to Work, Service time, Age, Work load, Average/day, Hit target, Disciplinary failure, Education, Son, Social drinker, Social smoker, Pet, Weight, Height, Body mass index, Absenteeism time in hours".

## References

Data Source: [Absenteeism at work](https://archive.ics.uci.edu/ml/datasets/Absenteeism+at+work)

- - -

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
