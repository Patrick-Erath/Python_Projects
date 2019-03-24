# decryptPDF.py : goes through  every PDF in a subfolder (and its subfolder)
# and decrypts the PDF with a provided password
import os
import PyPDF2
import sys
import re

password = sys.argv[1]

for root, dirs, files in os.walk(".", topdown=False):
	# Go through every PDF in a folder & subfolders
	for name in files:
		extension = os.path.splitext(name)[1]
		# Check if file is a pdf
		if(extension == '.pdf'):
			pdfFile = open(name, 'rb')
			pdfReader = PyPDF2.PdfFileReader(pdfFile)
			if(pdfReader.isEncrypted == True):
				try:
					pdfWriter =  PyPDF2.PdfFileWriter()
					pdfReader.decrypt(password)
					for pageNum in range(0, pdfReader.numPages):
						pageObj = pdfReader.getPage(pageNum)
						pdfWriter.addPage(pageObj)
					newName = re.sub('_encrypted', '_decrypted', name)
					newPDF = open(newName, 'wb')
					pdfWriter.write(newPDF)
					pdfFile.close()
					newPDF.close()
				except PyPDF2.utils.PdfReadError:
					print('Wrong password')