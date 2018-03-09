# -*- coding: utf-8 -*-

#! python3
# ! /usr/local/Cellar/python3/3.6.1

import openpyxl, pprint
import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

print('Opening workbook...')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population By Census Tract']

countyData = {}

# TODO:  fill in countyData with each county's population and tracts

print('Reading rows...')

for row in range(2,sheet.max_row + 1):
	# each row in the spreadsheet has data for one census tract
	state = sheet['B' + str(row)].value
	county = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value

# TODO:  open a new text file and write the contents of countyData to it

