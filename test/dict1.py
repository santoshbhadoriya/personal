try:
	counts=dict()
	n=input('Enter lenght of dict :')
	i=0
	while i < n :
		i += 1
		k=raw_input('Enter city name :')
		v=raw_input('Enter value :')
		counts[k]=v

	print 'Items in a dict are :', counts

	for k,v in counts.iteritems():
		print 'Entries are ------- :', k, v

	print r'Wanna Add(1), delete(2), Search(3), Modify(4) in dict......'

	x=input('Please enter your choice number')

	if x == 1:
		k=raw_input('Enter city name :')
		v=raw_input('Enter value :')
		counts[k]=v
	print 'Items in a dict now are  :', counts

	if x == 2:
		k=raw_input('Enter the city name you want to delete from dict :')
		del counts[k]
	print 'Items in a dict now are  :', counts

	if x == 3:
		city=raw_input('Enter the city name you want to search in dict :')

		for x,y in counts.iteritems():
			if x == city:
				print city, counts[city]

	if x == 4:
		city=raw_input('Enter the city name value you want to modify in dict :')
		for x,y in counts.iteritems():
                        if x == city:
				print 'Current values are ', city, counts[city]
				v=raw_input('Enter new value :')
				counts[city]=v
	print 'Items in a dict now are  :', counts

	#else:
	#	print 'Please type any of Add(1), delete(2), Search(3)'

except:
	print 'Please Enter numeric input....'
	
