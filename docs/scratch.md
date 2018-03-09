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

