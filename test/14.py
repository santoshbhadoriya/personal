#!/usr/bin/python
name=raw_input('Enter filename :')
handle=open(name, 'r')
text=handle.read()
print 'Text is :', text
words=text.split()
print 'Words are : ', words

counts=dict()
for word in words:
	counts[word]=counts.get(word,0) + 1

print 'Count is :', counts

for key in counts:
	print key,counts[key]

bigcount = None
bigword = None

for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print 'Max count is :', bigword,bigcount
