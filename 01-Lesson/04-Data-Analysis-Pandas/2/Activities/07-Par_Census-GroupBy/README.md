# Exploring Census Data

In this activity, you will use data from the 2016 Australian Census and create DataFrames with calculated totals and averages for each state.

## Instructions

1. Read in the [2016_rental_by_LGA.csv](Unsolved/Resources/2016_rental_by_LGA.csv) CSV file with Pandas.

2. Create a `GroupBy` object, where the data is grouped by state.

3. Create two new DataFrames from the `GroupBy` object: one with the total (sum) of each column and one with the average (mean) of each column.

4. Add a column to the totals DataFrame that is the sum of all the other columns.

5. Export the resulting tables to CSVs.

## References

Australian Census 2016, Rent (weekly) by Dwelling Structure (LGA), [Australian Bureau of Statistics](https://explore.data.abs.gov.au/vis?pg=0&df[ds]=CENSUS_2016_TOPICS&df[id]=ABS_C16_T26_LGA&df[ag]=ABS&df[vs]=1.0.0&fc=Rent%20%28weekly%29%20Ranges&fs[0]=Census%202016%2C0%7CGeneral%20Profiles%20for%20LGAs%23GEN_PROFILE_LGA_C16%23&fs[1]=Rent%20%28weekly%29%20Ranges%2C1%7CTotal%23TOT%23%7C%24200-%24224%238%23), filtered at source and then transformed and reduced in Pandas.

- - -

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
