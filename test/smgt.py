#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the sample output below.


largest = None
smallest = None

while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue
    if smallest is None:
        smallest = num 
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num


print "Maximum is", largest
print "Minimum is", smallest
