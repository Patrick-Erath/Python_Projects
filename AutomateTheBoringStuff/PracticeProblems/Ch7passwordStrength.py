import re
# passwordStrength.py : Checks that passwords follow the following requirement:
	# - 8 characters long 
	# - UPPER CASE
	# - lower case
	# - 1 digit 
	# tested on : https://regex101.com/r/aQ9vG2/1
passwords = ['passWORD', 'passworD233', 'Doensn', 'donut', 'Passworde875667', 'CatsDogs21']

#passwordRegex = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{10,}$')
passwordRegex = re.compile(r'''(
							^(?=.*?[0-9])   # Check for number
							(?=.*?[A-Z]) # Check for uppercase letter
							(?=.*?[a-z]) # Check for lowercase letter
							[a-zA-Z\d]{8,}$ # Check length
							)''',re.VERBOSE)
						
for password in passwords:
	w = passwordRegex.search(password)
	try: 
		print(w.group()+' <------GOOD password')
	except:
		print(password+'  <------WEAK password')
		continue

