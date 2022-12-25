#Definition
time = 0

def oneprime(x):
	y = 1
	x0 = x
	while x0 != 0:
		y = y + 1
		x0 = x % y
#		print y
	return y

def change(x):
	try:
		x = int (x)
		return x
	except:
		exit = raw_input('oh no.\nEnter to exit.' )
		quit()

#Main
number = change(raw_input('What is the number?\n'))
print number,'=',

while number > 1:
	prime = change(oneprime(number))
	number = number / prime
	if number == 1:
		print prime
	else:
		print prime,'*', 
	time = time + 1

if time == 1:
	print 'This is a prime.'
elif time == 0:
	print 'oh no.'
else: print 'This is not a prime.'

exit = raw_input('Enter to exit.' )