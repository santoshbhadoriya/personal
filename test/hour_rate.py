#!/usr/bin/python
try:
        inp = raw_input("Enter Hours:")
        hours = float(inp)
        inp = raw_input("Enter Rate:")
        rate = float(inp)
except:
        print "Error, please enter numeric input"
        quit()

print 'Entered Rate and Hours are ', rate,hours
if (hours <= 40):
        pay = hours*rate
else:
        pay = rate * 40 + (rate * 1.5 * (hours -40))
print 'Total amount to be paid is after calculation :', pay

