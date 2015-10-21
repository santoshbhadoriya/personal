#wap that prompts that user to enter int values each of two list
#prorgm should dispaly len are same,find out command elements,list are same or not

x=[]
z=[]
y=raw_input('Enter list here :')
while y!='':
        x.append(y)
        y=raw_input('Enter list here :')

print 'Given list is x=', x
m=[]
n=raw_input('Enter list here :')
while n!='':
        m.append(n)
        n=raw_input('Enter list here :')

print 'Given list is m=', m

if (len(x)==len(m)):
	print 'length of both list is same x=%s and m=%s' %(len(x),len(m))
else:
	print 'Length is different on both list x=%s and m=%s' %(len(x),len(m))

#common=list(set(x).intersection(m))
#if len(common) == 0:
#	print 'No common elements'
#else:
#	print 'Common elements in both list are : %s' %common

for i in m:
	if i in x:
		z.append(i)
#print z
if len(z) == 0:
	print 'No common elements'
else:
	print 'Common elements in both list are : z=', z
