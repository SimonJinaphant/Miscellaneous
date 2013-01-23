original = "QWERTYUIOPASDFGHJKLZXCVBNM"
shifted = "WERTYUIOP[SDFGHJKL;XCVBNM,"

message = "Hello Word"
new_message = ""
for i in range(len(message)):
	
	if ord(message[i]) >= 0x41 and ord(message[i]) <= 0x5a:
		new_message += shifted[shifted.find(message[i])+1]
	else:
	
		new_message += str(shifted[shifted.find(chr(ord(message[i])-0x20))+1]).lower()
		
print new_message