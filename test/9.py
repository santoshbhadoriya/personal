fhand=open('t1')
for line in fhand:
	line=line.rstrip()
	if line == '' :continue
	words=line.split()
	if words == [] : continue
	if words[0] != 'From' : continue
	print words[2]

