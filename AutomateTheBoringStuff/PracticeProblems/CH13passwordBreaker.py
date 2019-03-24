# passwordBreaker.py : this program attemps to guess the password of a PDF document
# by trying 44,000 basic english words as the password
import PyPDF2

text = open('dictionary.txt')
text = text.read()
words = text.split('\n')

pdfFileObj = open('meetingminute_encrypted.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
for word in words:
	print('Trying to break in with ' + word + '...')
	try: 
		if(pdfReader.decrypt(word) == 1):
			print('The password is :', word)
			break
		elif(pdfReader.decrypt(word.lower()) == 1):
			print('The password is :', word.lower())
			break
	except: 
		print('Could not determine the password')