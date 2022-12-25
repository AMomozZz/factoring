def fj(x):
	x0 = x
	z = 0
	y = 1
	while x0 > 1:
		y = y+1
		x1 = x0 % y
		if x1 == 0:
#			print y
			x0 = x0 / y
			y = 1
			z = z + 1
	return z

def change(x):
	try:
		x = int (x)
		return x
	except:
		print 'oh no.'
		quit()

number = raw_input('What is the number?')
number0 = fj(change(number))
if number0 == 1:
	print 'true'
elif number0 == 0:
	print 'oh no.'
else: print 'false'

raw_input('')