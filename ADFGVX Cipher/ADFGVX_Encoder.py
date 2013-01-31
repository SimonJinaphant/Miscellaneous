from re import sub
'''
	A python script for encrypting a message base on the German's ADFGVX encryption
	used in World War I

	This version has reduced code clarity, but has a better algorithm so if you want to 
	read the code clearly, without much problems, you're reading the wrong version...
	unless you have no problem reading long lambda functions, list comprehensions, 
	and dictionary comprehension: then you can carry on reading the code below :P
	
	However since I've commented the code to describe it, the clarity should still
	be there even if you can't understand much of the code
	
	Artefact #1 for Term 2 Socials 11
	- Simon Jinaphant
	
	Version 2.01
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
	'''
	cipher = lambda char: [(base[left_index],base[top_index]) 
							for left_index, row in enumerate(key_square)
		 					for top_index, letter in enumerate(row) if letter == char][0]

	ciphered_raw = [letter for char in sub(r'[^\w]','',message.lower()) 
							for letter in cipher(char)]
		
	return columnar_transposition(ciphered_raw)
			
			
def columnar_transposition(ciphered):
	'''
		Performs a column transposition on the ciphered letters and returns the message
		
		This is part 2 of the ADFGVX encryption. 

		1. Start by grouping the individual ciphered letters according to the key_word
		
		Since there is a pattern in the letters to be grouped per each key, we can simplify
		this to a dictionary comprehension, with a list comprehension for all the values.
		
		The value for each key can be found by taking the first letter at the index 
		corresponding to @count and stepping by the length of the @key_word
	'''
	
	new_table = {key_letter:ciphered[count::len(key_word)] 
						for count, key_letter in enumerate(key_word)}
	
	'''
		2. Perform an alphabetical sorting on the group, using the key of the group
			(which is the one of the base_word's letter), as the sorting key.
		
		3. Copy the letters in each group and concatenate it with the letters 
			from the other group, resulting in the complete encrypted message
	'''
	
	return "".join(["".join(v) for _k, v in sorted(new_table.iteritems(), key = lambda k1: k1[0])])
	

print cipher_message(raw_input("Enter a message: "))