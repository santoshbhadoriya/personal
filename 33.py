#wap that prompts the user to enter list of first name and stores that in a list
#the programs should display how many times the 'a' appers with in a list

x=[]
y=raw_input('Enter list here :')
while y!='':
	x.append(y)
	y=raw_input('Enter list here :')

print 'Given list is x=', x
z=raw_input('Enter the letter you want to search in given list :')
m=str(x)
count=m.count(z)
print 'total number of times letter %s occur in list is %s' %(z,count)
