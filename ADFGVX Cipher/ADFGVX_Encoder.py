from re import sub
'''
	A python script for encrypting a message base on the German's ADFGVX encryption
	used in World War I

	This version has reduced code clarity, so if you're wanting to read the code clearly,
	without much problems, you're reading the wrong version...unless you have no problem
	reading long lambda functions and list comprehensions, then you can carry on reading
	the code below :P
	
	However since I've commented the code to describe it, the clarity should still
	be there even if you can't understand much of the code
	
	Artefact #1 for Term 2 Socials 11
	- Simon Jinaphant
'''

base = "ADFGVX"			#For the letter lookup
key_word = "GERMAN"		#This is used in Part 2 of the encryption

#The key square is one of the two keys required to encode/decode a message
key_square = (('p','h','0','q','g','6'),
			  ('4','m','e','a','1','y'),
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

		@lambda cipher
			Returns a two element tuple containing the left and top ADFGVX letter 
			the input character corresponds to
			
			Note: The [0] is for extracting the tuple within the list, it's just a fancy 
			way of returning a single tuple only using list comprehension

		@lambda extract
			Returns an list of the individual alphanumeric characters within the message
	'''
	cipher = lambda char: [(base[left_index],base[top_index]) 
							for left_index, row in enumerate(key_square)
		 					for top_index, letter in enumerate(row) if letter == char][0]

	extract = lambda: [letter for word in message.lower().split() 
							for letter in sub(r'[^\w\s]','',word)]
	
	ciphered_raw = []
	
	for char in extract() :
		ciphered_raw.extend(cipher(char))
		
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
	final_message = []
	
	for count, key_letter in enumerate(key_word):
		new_table[key_letter] = [cipher_v for cipher_k, cipher_v in enumerate(ciphered_letters) 
									if cipher_k % len(key_word) == count]
	
	for ciphered_key, ciphered_value in sorted(new_table.iteritems(), key = lambda k1: k1[0]):
		final_message.extend(ciphered_value)
				
	return "".join(final_message)
	

print cipher_message(raw_input("Enter a message:"))