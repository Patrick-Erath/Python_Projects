# shortestDistance.py : This project is a code that works with distance.py, it reads all the times to a
# destination, then finds what the distances are to leave to each location

import openpyxl, datetime

# TODO: iterate over each country and find lowest time
# Create new excel sheet with lowest time of each country
wb = openpyxl.load_workbook('Time.xlsx')
sheet = wb.active
dicts = {}


for row in range(2, sheet.max_row+1):
	# Get values from excel sheet
	city = sheet['A' + str(row)].value
	distance = sheet['B' + str(row)].value
	timestamp = sheet['C' + str(row)].value

	# Populate dictioanry
	dicts.setdefault(city, {})
	dicts[city].setdefault(timestamp, distance)


for city in dicts:
	print('-'*40)
	print('The travel times to '+city+' are :')
	print('-'*40)
	for time in dicts[city]:
		print(dicts[city][time]+' on the date '+str(time))

		










