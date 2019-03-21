# CombinePDF.py - Combines all the PDFs in the current working directory 
# into a single PDF

import PyPDF2, os

# Get all PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)
	pdfFiles.sort(key=str.lower) # Sort files by alphabetical order
	pdfWriter = PyPDF2.PdfFileWriter()

	# Loop through all PDF files
	for filename in pdfFiles:
		pdfFileObj = open(filename, 'rb') # Open file in readbinary & pass to object
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj) # Creae object for reading file
		# Loop through all pages (except the first) and add them
		for pageNum in range(1, pdfReader.numPages): # From 1 to max pages in pdfReader object
			pageObj = pdfReader.getPage(pageNum) # Get page of pageNum from pdfReader Obj and set to pageObj
			pdfWriter.addPage(pageObj) # Add pageObj to PDF writer

	# Save the resulting file to a PDF
	pdfOutput = open('combined.pdf', 'wb')
	pdfWriter.write(pdfOutput)
	pdfOutput.close()
