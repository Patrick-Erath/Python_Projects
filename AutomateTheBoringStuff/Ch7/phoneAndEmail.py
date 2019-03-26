# phoneAndEmail.py : finds phone numbers and email addresses on the clipboard

import pyperclip, re

# Phone regex
phoneRegex = re.compile(r'''(
				(\d{3}|\(\d{3}\))? # Area code, ie : 777 OR 777 in parth., not necessary
				(\s|-|\.) # Seperator, ie space, - or .
				(\d{3}) # Three digits
				(\s|-|\.) # Seperator
				(\d{4}) # Four digits
				(\s*(ext|x|ext.)\s*(\d{2,5}))? # Extension
				)''', re.VERBOSE)

# Email regex
emailRegex = re.compile(r'''(
				[a-zA-Z0-9._%+-]+ # Username, ie josh
				@				  # Hyphen
				[a-zA-Z0-9.-]+	  # Domain name, ie hotmail
				(\.[a-zA-z]{2,4}) # Domain extension, ie .ca
				)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNumber = '-'.join([groups[1],groups[3], groups[5]])
	if groups[8] != '':
		phoneNumber += ' x:' + groups[8]
	matches.append(phoneNumber)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

# Copy results to clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers of email addresses found.')