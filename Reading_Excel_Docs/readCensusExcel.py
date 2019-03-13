import openpyxl, pprint
print('Opening workbook..')

wb = openpyxl.load_workbook('../automate_online-materials/censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countryData = {}

#TODO : Fill in coutnryData with each country's population and tracts.
print('Reading rows ... ')
for row in range(2, sheet.max_row + 1):
	#Each row in the spreadsheet has data for one census tracts
	state	 = sheet['B' + str(row)].value
	country  = sheet['C' + str(row)].value
	pop  	 = sheet['D' + str(row)].value


