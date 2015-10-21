numlist=list()
while True:
	inp=raw_input("Enter a number : ")
	if inp == '':break
	value = float(inp)	
	numlist.append(value)

print 'Current list is :', numlist

average = sum(numlist) / len(numlist)
print 'Average', average
