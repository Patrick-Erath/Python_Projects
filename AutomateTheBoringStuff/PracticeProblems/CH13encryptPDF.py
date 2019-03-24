# encryptPDF.py : goes through  every PDF in a subfolder (and its subfolder)
# and encrypts the PDF with a password and deletes the original file
import os
import PyPDF2
import sys

password = sys.argv[1]

for root, dirs, files in os.walk(".", topdown=False):
	# Go through every PDF in a folder & subfolders
	for name in files:
		extension = os.path.splitext(name)[1]
		# Check if file is a pdf
		if(extension == '.pdf'):
			# Encrypt file
			pdfFile = open(name, 'rb')
			pdfReader = PyPDF2.PdfFileReader(pdfFile)
			pdfWriter =  PyPDF2.PdfFileWriter()
			for pageNum in range(pdfReader.numPages):
				pdfWriter.addPage(pdfReader.getPage(pageNum))
			pdfWriter.encrypt(password)
			newName = name+'_encrypted.pdf'
			resultPdf = open(newName, 'wb')
			pdfWriter.write(resultPdf)
			resultPdf.close()
			# Delete old file
			os.remove(name)
			
print('All pdf files have been encrypted')

				