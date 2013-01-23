alphabet = [chr(0x41+count) for count in range(26)]
	
def encode(message, cipher_key):
	
	encoded_message = ""
		
	for i in range(len(message)):
		key_index = alphabet.index(cipher_key[i % len(cipher_key)])
		message_index = alphabet.index(message[i])
		
		encrypted_index = (key_index+message_index)%26
		
		#print (key_index,message_index, encrypted_index)
		
		encoded_message += alphabet[encrypted_index]
		
	return encoded_message
		
def decode(message, cipher_key):
	
	decoded_message = ""
	
	for i in range(len(message)):
		pre_key_index = alphabet.index(message[i])
		key_index = alphabet.index(cipher_key[i % len(cipher_key)])
		
		decoded_index = pre_key_index-key_index
		
		if decoded_index < 0:
			decoded_index +=26
		
		#print (key_index,decoded_index,pre_key_index)
		
		decoded_message+=alphabet[decoded_index]
		
	return decoded_message
		
print encode("THECAKEISALIE","GLADOS")
print decode("ZSEFOCKTSDZAK","GLADOS")

