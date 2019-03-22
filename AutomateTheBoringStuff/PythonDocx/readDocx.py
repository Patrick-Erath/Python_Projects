import docx

def getText(fileName):
	doc = docx.Document(fileName)
	fullText = []
	for para in doc.paragraphs:
		fullText.append(' '+para.text)
	return ' '.join(fullText)
