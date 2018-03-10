# -*- coding: utf-8 -*-

#! python3
# ! /usr/local/Cellar/python3/3.6.2

# USAGE
# python3 read_census_excel_030918_1.py

import openpyxl, pprint
import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

print('Opening workbook...')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']

countyData = {}

# fill in countyData with each county's population and tracts

print('Reading rows...')

for row in range(2,sheet.max_row + 1):
	# each row in the spreadsheet has data for one census tract
	state = sheet['B' + str(row)].value
	county = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value

	# make sure the key for this state exists
	countyData.setdefault(state,{})
	logging.debug('The state name %s key has been created.' % (state))

	# make sure the key for this county in this state exists
	countyData[state].setdefault(county,{'tracts':0,'pop':0})
	logging.debug('The county name %s key has been created with 0 values within its dictionary.' % (county))

	# each row represents one census tract, so increment by 1
	countyData[state][county]['tracts'] += 1
	logging.debug('Current value of tracts is:  ')
	logging.debug(countyData[state][county]['tracts'])

	# increase the county pop by the pop in this census tract
	countyData[state][county]['pop'] += int(pop)
	logging.debug('Current value of population is: %i' % (countyData[state][county]['pop']))

# open a new text file and write the contents of countyData to it

print('Writing results...')

resultFile = open('census2010.py','w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')

