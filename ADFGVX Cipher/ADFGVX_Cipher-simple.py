from re import sub
'''
	A python script for encrypting a message base on the German's ADFGVX encryption
	used in World War I
	
	This version has better code clarity, I've simplified most of the code, in a more
	easier-to-read manner
	
	I've commented the code to describe it, the clarity should still be there even
	if you can't understand much of the code
	
	Artefact #1 for Term 2 Socials 11
	- Simon Jinaphant
'''

base = "ADFGVX"			#For the letter lookup
key_word = "GERMAN"		#This is used in Part 2 of the encryption

#The key square is one of the two keys required to encode/decode a message
key_square = (('p','h','0','q','g','6'),
			  ('4','m','e','a','l','y'),
			  ('l','2','n','o','f','d'),
			  ('x','k','r','3','c','v'),
			  ('s','5','z','w','7','b'),
			  ('j','9','u','t','i','8'))

						
def cipher_message(message):
	'''
		Given an input, return the ADFGVX encrypted string of all alphanumeric characters
		
		This function is part 1 of the encryption
		
		1. Extract the individual alphanumeric characters in the message and
			calling the cipher_letter() function to look up the position on the table,
			giving us the new secret two digit word
		 
		2. Pass a list containing the ciphered alphanumeric characters to part 2 and await
			the return results of the final message
	'''
	
	def cipher_letter(char):
		'''
			Returns a two element tuple containing the left and top ADFGVX letter 
			the input character corresponds to
		'''
		for left_index, row in enumerate(key_square):
			for top_index, letter in enumerate(row):
				if letter == char:
					return (base[left_index],base[top_index])

	def extract_char():
		'''
			Returns an list of the individual alphanumeric characters within the string
			passed in
		'''
		extracted = []
		
		for word in message.lower().split():
			for letter in sub(r'[^\w\s]','',word):
				extracted.append(letter)
				
		return extracted
						
						
	ciphered_raw = []
	
	for char in extract_char():
		ciphered_raw.extend(cipher_letter(char))
			
	return columnar_transposition(ciphered_raw)
			

def columnar_transposition(ciphered_letters):
	'''
		Performs a column transposition on the ciphered letters and returns the message
		
		This is part 2 of the ADFGVX encryption. 
		
		1. Start by grouping the individual ciphered letters according to the key_word
		
		2. Perform an alphabetical sorting on the group, using the key of the group
			(which is the one of the base_word's letter), as the sorting key.
		
		3. Copy the letters in each group and concatenate it with the letters 
			from the other group, resulting in the complete encrypted message, and return 
			back to the cipher_message() function
		
	'''
	new_table = {}
	final_message = ""
	
	for count, key_letter in enumerate(key_word):
		new_table[key_letter] = []
		for cipher_v, cipher_k in enumerate(ciphered_letters):
			if cipher_v % len(key_word) == count:
				new_table[key_letter].append(cipher_k)

	new_table = sorted(new_table.iteritems(), key = lambda(v1, k1): v1)
	
	for v, k in new_table:
		final_message += k[0]+k[1]
				
	return final_message
	

print cipher_message(raw_input("Enter a message:"))