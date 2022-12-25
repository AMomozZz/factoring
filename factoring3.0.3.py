#Definition
import math
#import random
from definition.factoring import *
time = 0
primey = 2
lenth = 0
again = 1
extraction = 0
#time_r = 1
key = "\n\n" #Don't use single quotes here, use double quotes.

with open('data/process.txt','a+') as process:
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
	w_f(process,'number %d: %d = '%(c,number))

	if number == 1:
		print '1'
		w_f(process,'1')
		time = 1

	while number > 1:
		extraction = int(math.floor(number ** 0.5))
		prime = oneprime(number,primey,extraction)
		number = number / prime
		primey = prime
		if number == 1:
			print prime
			w_f(process,'%d'%prime)
		else:
			print prime,'*', 
			w_f(process,'%d * '%prime)
		time = time + 1

	lenth = countnumber(number) + 3

	if time == 1:
		print 'This is a prime number.'
#	elif time == 0:
#		print '\b' * lenth + 'oh no.' + ' ' * (lenth-6)
	else: 
		print 'This is the product of %s prime numbers.'%str(time)

#	soundx()

	print(' ')
	w_f(process,'\n')

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