import openpyxl, pprint
print('Opening workbook..')

wb = openpyxl.load_workbook('../automate_online-materials/censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countryData = {}

#TODO : Fill in coutntry Data with each country's population and tracts.
print('Reading rows ... ')
for row in range(2, sheet.max_row + 1):
	#Each row in the spreadsheet has data for one census tracts
	state	 = sheet['B' + str(row)].value
	country  = sheet['C' + str(row)].value
	pop  	 = sheet['D' + str(row)].value

	# Make sure the key for this state exists
	countryData.setdefault(state, {})
	# Make sure the key for this country in this state exists
	countryData[state].setdefault(country, {'tracs':0, 'pop':0})

	# Each row represents one census tract, so increment by one.
	countryData[state][country]['tracs'] += 1
	countryData[state][country]['pop'] += int(pop)

# Open a new text-file and write the contents of countryData to it
print('Writing results ... ')
resultFile = open('census2010.py', 'w')
resultFile.write('allData =' + pprint.pformat(countryData))
resultFile.close()
print('Done.')