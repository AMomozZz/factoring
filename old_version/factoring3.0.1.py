#Definition
import math
#import winsound
#import random
time = 0
primey = 2
lenth = 0
again = 1
extraction = 0
#time_r = 99999999999999
key = "\n\n" #Don't use single quotes here, use double quotes.

def out(x):
	exit = raw_input('Enter to exit.')
	if exit == 'show code':
		print str(x)
		raw_input('Enter to exit.')
	quit()

def oneprime(x,y,z):
	y = y - 1
	x0 = x
	while x0 != 0:
		y = y + 1
		x0 = x % y
#		print y
		if y >= z:
			break
	if x0 == 0:
		return y
	elif y >= z:
		return x

def change(x):
	try:
		x = int (x)
		return x
	except:
		print 'Please give me a number.'
		x = 0
		return x

def countnumber(x):
	x = str(x)
	x = int(len(x))
	return x

#def soundx():
#	winsound.Beep(600,300)

#Main
while again == 1:

#	time_r += 1
#	number = time_r
#	print('number %s')%str(time_r)

	time = 0
	primey = 2

	number = change(raw_input('The number is: '))
#	number = random.randint(0, 99999999999999999999)
#	print('the number has %s bits.')%countnumber(number)

	if number == 0:
		continue
	print number,'=',

	if number == 1:
		print '1'
		time = 1

	while number > 1:
		extraction = int(math.floor(number ** 0.5))
		prime = oneprime(number,primey,extraction)
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

#	soundx()

	print ''

	a = str(raw_input('Do you want to do another factorization? Y/N (Press Enter means yes.)\n'))
#	a = 100
	if a == 'N' or a == 'n' :
#	if time_r == a:
		break
	elif a == 'Y' or a == 'y' :
#	elif time_r < a:
		pass

#Out and show code
out(key)