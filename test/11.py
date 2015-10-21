counts=dict()
names=list()
inp=raw_input('Enter names :')
while inp != '':
	names.append(inp)
	inp=raw_input('Enter names :')
print 'Names entered are : ', names
for name in names:
	counts[name]=counts.get(name,0) + 1

print 'Count of names is : ', counts

