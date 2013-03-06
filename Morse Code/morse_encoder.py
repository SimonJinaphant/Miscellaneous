'''
	A simple morse code encoding program
	Social Studies 11 - Artifact 2
	
	- Simon Jinaphant & Gopal Sharma
	
	This program has simplified source code with comments explaining the process,
	if you don't understand programming it's okay, the comments should be able to
	guide you through what's happening
'''


table = {
	'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
	'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
	'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'._.', 
	'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
	'Y':'-.--', 'Z':'--..', ' ':' '
}

'''
	We start off the program by getting the user's message and turning all
	the letters to it's capital form since we don't care about the case of
	encoded message in the end
'''
input_message = raw_input("Enter a message for encoding: ").upper()

'''
	Next we go through each individual letter in the input message
	We look up the morse code sequence on the table for each letter
	and add it the the list of our finished encoded message
'''
encoded_message = []

for word in input_message:
	for letter in word:
		encoded_message.append(table[letter])

'''
	Finally we go through the list again and group each letter together,
	printing it out to the screen in the end
'''
print " ".join([char for char in encoded_message])