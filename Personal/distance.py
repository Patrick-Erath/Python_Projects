# distance.py : This project uses Google Maps API to find the distance between a starting address
# and multiple destinations. The project then writes the time to each destination to an excel file
# This was a personal project to determine the best time to leave for a destination

import googlemaps, datetime, openpyxl
from openpyxl.styles import Font

# TODO: make this code run every hour 

gmaps = googlemaps.Client(key='YOUR_GOOGLE_API_KEY_HERE')

startingAddress = 'Schweinfurt, Germany'
destinations = ['Amsterdam', 'Berlin', 'Brussels','Stuttgart','Sächsische Schweiz','Allgaü','Garmish-Partenkirchen']
dictionary = {}

print('Getting distances using GoogleMaps API...')
for i in range(len(destinations)):
	try:
		now = datetime.datetime.now()
		directions_result = gmaps.directions("Schweinfurt, Germany",
		                                     destinations[i],
		                                     mode="driving",
		                                     departure_time=now)
		# Populate dictionary
		dictionary[destinations[i]]=directions_result[0]['legs'][0]['duration']['text']
		#print('The distance to '+destination+' is '+directions_result[0]['legs'][0]['duration']['text'])
	except: 
		print('Error')

# Output to excel file
print('Writing distances to Excel sheet...')
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Destination Times'
# Init names
fontObj1 = Font(name='Times New Roman', bold=True)
sheet.cell(row=1, column=1).value='Destination'
sheet.cell(row=1, column=2).value='Driving Time'
sheet.cell(row=1, column=2).value='Time Taken'
sheet['A1'].font=fontObj1
sheet['B1'].font=fontObj1
sheet['C1'].font=fontObj1
rowNum=2
now = datetime.datetime.now()
now = now.replace(second=0, microsecond=0)
for destination in dictionary:
	sheet.cell(row=rowNum, column=1).value=destination
	sheet.cell(row=rowNum, column=2).value=dictionary[destination]
	sheet.cell(row=rowNum, column=3).value=now
	rowNum+=1
wb.save('Time.xlsx')
print('Done')
