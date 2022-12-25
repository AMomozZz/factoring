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
with open('data/process.txt','r') as process:
	all_process = str(process.readline())
if all_process == '':
	with open('data/process.txt','a+') as process:
		process.write('0\n')
		process.seek(0,0)
		all_process = str(process.read())
process = open('data/process.txt','a+')
all_process = str(process.readline())
timex = all_process.find('\n',0)
time_ = int(all_process[0:timex])

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
		x = 0
		return x

def countnumber(x):
	x = str(x)
	x = int(len(x))
	return x

def search(a,b):
	x = 0
	for letter in a:
		if letter == b:
			x += 1
	return x

def w_f(x):
	process.write(x)
	process.flush()

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

	if number <= 0:
		print 'Please give me a meaningful number.'
		continue
	print number,'=',
	process.seek(0,0)
	a = process.read()
	b = '\n'
	c = search(a,b) - time_
	process.seek(0,0)
	w_f('number %d: %d = '%(c,number))

	if number == 1:
		print '1'
		w_f('1')
		time = 1

	while number > 1:
		extraction = int(math.floor(number ** 0.5))
		prime = oneprime(number,primey,extraction)
		number = number / prime
		primey = prime
		if number == 1:
			print prime
			w_f('%d'%prime)
		else:
			print prime,'*', 
			w_f('%d * '%prime)
		time = time + 1

	lenth = countnumber(number) + 3

	if time == 1:
		print 'This is a prime number.'
#	elif time == 0:
#		print '\b' * lenth + 'oh no.' + ' ' * (lenth-6)
	else: 
		print 'This is the product of %s prime numbers.'%str(time)

#	soundx()

	print ''
	w_f('\n')

	a = str(raw_input('Do you want to do another factorization? Y/N (Press Enter means yes.)\n'))
#	a = 100
	if a == 'N' or a == 'n' :
#	if time_r == a:
		break
	elif a == 'Y' or a == 'y' :
#	elif time_r < a:
		pass

process.close()

#Out and show code
out(key)