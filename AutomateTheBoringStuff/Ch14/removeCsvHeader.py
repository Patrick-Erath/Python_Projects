# removeCsvHeader.py : removes the header from all CSV files in the current
# working directory
import csv, os

os.makedirs('headerRemoved', exist_ok=True) # Creates path

# Loop through each file in the current working directory
for csvFileName in os.listdir('.'):
	if not csvFileName.endswith('.csv'):
		continue #skip non-csv files (go to next file in for loop)

	print('Removing header from ' + csvFileName + '...')
	# Remove the CSV file in (skipping first row)
	csvRows = []
	csvFileObj = open(csvFileName)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num == 1:
			continue # skip first row
		csvRows.append(row)
	csvFileObj.close()

	# Write out the CSV file
	csvFileObj = open(os.path.join('headerRemoved', csvFileName), 'w', newline='')
	csvWriter = csv.writer(csvFileObj) # Create new csv file object
	for row in csvRows:
		# Add each row to new csv file
		#print(row)
		csvWriter.writerow(row)
	csvFileObj.close()

