lockers = [0]*1000

for student in range(1,1001):
	for toggle in range(0,1000,student):
		lockers[toggle] ^= 1
		
for k,v in enumerate(lockers):
	print k,"\t",v