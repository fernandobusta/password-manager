#!/usr/bin/env python3

letter_for_n = {
	'a': 4, 
	'b': 5, 
	'c': 7, 
	'ç': 766,
	'd': 11, 
	'e': 45, 
	'f': 65, 
	'g': 6, 
	'h': 34, 
	'i': 35, 
	'j': 38, 
	'k': 102, 
	'l': 90, 
	'm': 44, 
	'n': 66,
	'ñ': 970, 
	'o': 89, 
	'p': 12, 
	'q': 43, 
	'r': 23, 
	's': 26, 
	't': 93, 
	'u': 75, 
	'v': 29, 
	'w': 1, n_for_letter = {
    1 : 'h',
    2 : 't',
    3 : 'yuy',
    4 : 'cap',
    5 : 'me',
    6 : 'go',
    7 : 'rt',
    8 : 'fo',
    9 : 'siuu',
    0 : 'que'
}
	'x': 0, 
	'y': 59, 
	'z': 2
}


n_for_letter = {
	1 : 'h',
	2 : 't',
	3 : 'yuy',
	4 : 'cap',
	5 : 'me',
	6 : 'go',
	7 : 'rt',
	8 : 'fo',
	9 : 'siuu',
	0 : 'que'
}

def encode(pwd):
	# Give the pwd and does the operation,
	# aka encodes the string
	encoded = []

	# pwd is a string
	for i in pwd.strip():

		# Turn upper case letter into an int
		# with '_' in front
		if i.isalpha() and i.isupper():
			for k, v in letter_for_n.items():
				if i.lower() == k:
					# '_n' where n is an int
					encoded.append(f'_{str(v)}')
					break

		# Turn lower case letter into an int
		elif i.isalpha() and i.islower():
			for k, v in letter_for_n.items():
				if i == k:
					encoded.append(str(v))
					break

		# Turn int into a seq of letters
		elif i.isdigit():
			for k, v in n_for_letter.items():
				if int(i) == k:
					encoded.append(v)
					break

		# i is a sign or another ch
		else:
			# and we don't change it
			encoded.append(i)

	# Returns a list to store in DB
	return encoded



def decode(encoded_pwd):
	# Give the pwd encoded and does the operation,
	# Aka decodes the string
	decoded = []

	# encoded_pwd is a list
	for i in encoded_pwd:
		
		# Checking to see if it is a capital letter
		# Aka: '_n', where n is an int
		if len(i) > 1 and i[0] == '_':
			# Extracting the number
			n = int(i[1:])
			for k,v in letter_for_n.items():
				if n == v:
					decoded.append(k.upper())
					break

		# Turn i into a lower case letter
		elif i.isdigit():
			for k, v in letter_for_n.items():
				if int(i) == v:
					decoded.append(k)
					break

		# Turn i into a number
		elif i.isalpha():
			for k, v in n_for_letter.items():
				if i == v:
					decoded.append(str(k))
					break

		# Leave i as it is, aka a sign
		else:
			decoded.append(i)

	# Return a string for the GUI to display
	pwd = ''.join(decoded)
	return pwd




































