reverse_table = {
	' ':' ', '.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E',
	'..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K',
	'.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q',
	'._.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W',
	'-..-':'X', '-.--':'Y', '--..':'Z'
}

message = [[dots_n_dash for dots_n_dash in code.split()] 
			for code in raw_input("Enter a message for encoding: ").split("   ")]
			
decoded = [[reverse_table[letter] for letter in word] for _, word in enumerate(message)]
	
print " ".join(["".join(final_word) for final_word in decoded])