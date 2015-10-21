#!/usr/bin/python
import os,sys
inp=raw_input('Enter rpm name: ')
if not os.system("rpm -qa |grep "+inp): 
	print 'Packge is already installed'
else:
	print 'Package is not installed'
print ""
#print "Yum Repository as below: "
#os.system("\nyum repolist")


