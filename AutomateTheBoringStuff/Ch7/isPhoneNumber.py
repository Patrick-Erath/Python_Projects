def isPhoneNumber(text):
	if text[3] != '-' or text[7] != '-' or len(text)!= 12:
		return False
	for i in range(0, 12):
		if i!=3 and i!=7:
			if not text[i].isdecimal():
				return False;	
	return True

message = 'meet me tonight at Brozington station call me at 514-977-9921 to confirm'
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print('Found number:', chunk)
		break