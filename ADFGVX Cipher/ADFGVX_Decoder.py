'''
	A python script for decrypting a message base on the German's ADFGVX encryption
	used in World War I
	
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
			  
def reverse_transposition(message):
	'''
		Given an input, return the ADFGVX decrypted string
		
		This function is part 1 of the decryption, it's also the most pain-in-the-@$$
		part of the entire program.
		
		Good news is: since you (the reader) didn't have to spend your time thinking and 
		writing this algorithm from 11:27am to 5:53pm, it's a lot simple to explain 
		via the comments. If you want to understand the code, good luck it was a 
		massive headache and yet a fun challenge writing it...
	'''

	def get_capacity(key_letter):
		'''
			Sub-step 1.	Determines how much element(s) a certain key contains when 
						compared with the original key_word. Some key may have more	
						or less than the others if the ciphered message has an unequal 
						length when compared the key_word
		'''
		capacity = divmod(len(message),len(key_word))
	
		return capacity[0] if key_word.index(key_letter) >= capacity[1] else capacity[0]+1
	
	'''
		Step 1.	Organize the table to contain each letter of the ciphered message when 
				read from top to bottom
	'''
	
	sorted_table = {key_letter:list() for key_letter in key_word}
	start_index = 0
	
	for key, letter in sorted(sorted_table.iteritems(),key=lambda k:k[0]):
		end_index = get_capacity(key)
		sorted_table[key].extend(message[start_index:start_index+end_index])
		start_index += end_index
	
	'''
		Step 2.	Reorganize table to match original table the cipher algorithm creates
				using the key_word
	'''
	raw_form = [raw_letter for raw_key, raw_letter in sorted(sorted_table.iteritems(),
							key=lambda k:key_word.index(k[0]))]
	
	'''
		Step 3.	Reads all the letter row by row
		
		There will be an index-out-of-bounds exception thrown when some keys have
		more or less elements in them, so we can't simplify this to a list comprehension
	'''

	final_form = []
									
	for x, _x in enumerate(max(raw_form, key=len)):
		for y, _y in enumerate(raw_form):
			try:
				final_form.append(raw_form[y][x])
			except:
				continue
				
	search_square(final_form)
	
	
def search_square(cipher):
	'''
		Given the raw ADFGVX string, return the decrypted message
		
		This is part 2 of the decryption, and also the easiest :D
		
		Step 1. From the given cipher, look up the decrypted letter for every 2
				letters the string contain, and store it in a list
		
		Step 2. Print the list...that's it you're done...
	'''
	final_message = [key_square[base.index(cipher[i])][base.index(cipher[i+1])]
		for i in xrange(0,len(cipher),2)]
		
	print "".join(final_message)
	

reverse_transposition(raw_input("Enter the ciphered code:"))