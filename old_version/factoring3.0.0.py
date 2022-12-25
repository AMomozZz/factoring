#Definition
time = 0
primey = 2
lenth = 0
again = 1
key = "\n\n" #Don't use single quotes here, use double quotes.

def out(x):
	exit = raw_input('Enter to exit.')
	if exit == 'show code':
		print str(x)
		raw_input('Enter to exit.')
	quit()

def oneprime(x,y):
	y = y - 1
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
		print 'Please give me a number.'
		out(key)
		
def countnumber(x):
	x = str(x)
	x = int(len(x))
	return x

#Main
while again == 1:
	
	time = 0
	primey = 2
	lenth = 0
	again = 1
	
	number = change(raw_input('The number is: '))
	print number,'=',

	if number == 1:
		print '1'
		time = 1

	while number > 1:
		prime = oneprime(number,primey)
		number = number / prime
		primey = prime
		if number == 1:
			print prime
		else:
			print prime,'*', 
		time = time + 1

	lenth = countnumber(number) + 3

	if time == 1:
		print 'This is a prime number.'
	elif time == 0:
		print '\b' * lenth + 'oh no.' + ' ' * (lenth-6)
	else: 
		print 'This is the product of %s prime numbers.'%str(time)
	
	a = str(raw_input('Do you want to do another factorization? Y/N (Press Enter means yes.)\n'))
	if a == 'N' or a == 'n':
		again = 0
	elif a == 'Y' or a == 'y':
		again = 1

#Out and show code
out(key)