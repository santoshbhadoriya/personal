fname=raw_input('Enter the file name :')
try:
	fhand=open(fname)
except:
	print 'File cannot be openned :',fname
	exit()
count=0
for line in fhand:
	if line.startswith('fun'):
		count=count+1
print 'There were',count,'lines in ',fname
