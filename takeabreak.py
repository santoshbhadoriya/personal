#!/usr/bin/python
import webbrowser
import time

total_breaks = 3
break_count = 0

print ("This program started on "+time.ctime())
while (break_count < total_breaks):
	time.sleep(10)
	webbrowser.open("https://www.udacity.com/course/viewer#!/c-ud036/l-993460168/m-1015728594")
	break_count = break_count + 1

