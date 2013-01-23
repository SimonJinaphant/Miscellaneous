import re

def type_check(unknown_type):
	if re.search("\A[+-]?\d+$",unknown_type):
		return unknown_type+"\t"+"int"
		
	elif re.search("\A[+-]?\d+\.\d*$", unknown_type):
		return unknown_type+"\t"+"float"
		
	else:
		return unknown_type+"\t"+"String"
		
print type_check("14")
print type_check("0")
print type_check("1032")
print type_check("-0")
print type_check("-5")
print type_check("+53")

print type_check("14.0")
print type_check("59.")
print type_check("-1.0")

print type_check("Hello")
print type_check("H3lL0")
print type_check("1GG")


