counts=dict()
names=list()
inp=raw_input('Enter names :')
while inp != '':
        names.append(inp)
        inp=raw_input('Enter names :')
print 'Names entered are : ', names
for name in names:
        if name not in counts:
                counts[name]=1
        else:
                counts[name]=counts[name] + 1
print 'Count of names is : ', counts

