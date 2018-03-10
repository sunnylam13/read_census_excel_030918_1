# Scratch Notes

## Friday, March 9, 2018 6:17 PM

the data structure

each state shorthand maps to another dictionary

so dict within a dict

the keys are strings of the county names in the state

each county name will then map to a dict with just 2 keys `tracts` and `pop`

which map to the number of census tracts and population for the county

	{
		'AK':{'Aleutians East':{'pop':3141,'tracts':1},'Aleutians West':{'pop':5561,'tracts':2},'Bethel':{'pop':17013,'tracts':3},'Bristol Bay':{'pop':997,'tracts':1},ETC}
	}	

if it was stored in `countyData`

	>>> countyData['AK']['Anchorage']['pop']
	291826
	>>> countyData['AK']['Anchorage']['tracts']
	55

`countyData` dict keys look kind of like...

	countyData[state abbrev][county]['tracts']
	countyData[state abbrev][county]['pop']

these rows do the calculation work

	# each row represents one census tract, so increment by 1
	countyData[state][county]['tracts'] += 1

	# increase the county pop by the pop in this census tract
	countyData[state][county]['pop'] += int(pop)

WARNING:  you can't add a county dict as the value for a state abbrev key name until the key already exists in `countyData`...

	# make sure the key for this state exists
	countyData.setdefault(state,{})

EXAMPLE:  

	countyData['AK']['Anchorage']['tracts'] += 1 will cause an error if the 'AK' key doesn't exist

to make sure the state key name is in your data you need to call the `setdefault()` method to set a value if one doesn't already exist for `state`...

on the same note...

each of the `countyData` dicts for each state needs its own dict as the value of each county key name...

in turn each of *those* dicts needs keys `tracts` and `pop`...  that start with integer value `0`...

	# make sure the key for this county in this state exists
	countyData[state].setdefault(county,{'tracts':0,'pop':0})

`setdefault()` does nothing if the key already exists so there's no issue using it a ton...

## Friday, March 9, 2018 6:36 PM

Ran with an error:

	MacBook-Air:read_census_excel sunnyair$ clear
	MacBook-Air:read_census_excel sunnyair$ python3 read_census_excel_030918_1.py
	Opening workbook...
	Traceback (most recent call last):
	  File "read_census_excel_030918_1.py", line 14, in <module>
	    sheet = wb['Population By Census Tract']
	  File "/usr/local/lib/python3.6/site-packages/openpyxl/workbook/workbook.py", line 247, in __getitem__
	    raise KeyError("Worksheet {0} does not exist.".format(key))
	KeyError: 'Worksheet Population By Census Tract does not exist.'
	MacBook-Air:read_census_excel sunnyair$

Except when I run it in the interpreter it works fine:

	MacBook-Air:read_census_excel sunnyair$ python3
	Python 3.6.2 (default, Sep  2 2017, 17:15:07)
	[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import openpyxl, pprint
	>>> wb = openpyxl.load_workbook('censuspopdata.xlsx')
	>>> sheet = wb['Population by Census Tract']
	>>> sheet.max_row
	72865
	>>> sheet['A2'].value
	'01001020100'
	>>>

## Friday, March 9, 2018 9:37 PM

`pprint.pformat()` creates a string that's also formatted as valid Python code...

	resultFile = open('census2010.py','w')

results in you creating a Python program from a Py program...

also lets you import it like any other Python module...

`read_census_excel_030918_1.py` only had to be used once as throwaway code...

once the results are saved to `census2010.py`, you just `import census2010`...

	>>> import os
	>>> import census2010
	>>> census2010.allData['AK']['Anchorage']
	{'pop': 291826, 'tracts': 55}
	>>> anchoragePop = census2010.allData['AK']['Anchorage']['pop']
	>>> print('The 2010 population of Anchorage was ' + str(anchoragePop))
	The 2010 population of Anchorage was 291826
	>>>

ABSP:  460

## Friday, March 9, 2018 9:46 PM

Ideas for Similar Programs...

in business, spreadsheets can become bloated and hard to use...

a program that can analyze a sheet is handy...

what could it do?

* compare data across multiple rows

* open multiple Excel files and compare data between spreadsheets (assuming the structures are similar)

* check whether a spreadsheet has blank rows or bad data in any cells and give a warning

* read data from a sheet and use it as input for Python programs...

