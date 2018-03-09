# Read Census Data from a Spreadsheet

A program that goes through census data spreadsheets row by row and tallies up the population numbers.  It also calculates the statistics for each county.

## What the Program Does

* reads Excel spreadsheet data

* counts the number of census tracts in each county

* counts the total population of each county

* prints the results

## What the Code Does

* open and read cells of an Excel doc with `openpyxl`

* calculate all the tract and population data and store it in a data structure

* write the data structure to a text file with the `.py` extension using the `pprint` module

## Test Data

	read_census_excel/censuspopdata.xlsx

