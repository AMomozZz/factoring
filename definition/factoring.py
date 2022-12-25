import winsound

__all__ = ['change', 'countnumber', 'out', 'w_f', 'soundx', 'search', 'oneprime','findx','compare']

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

def out(x = 'not given'):
	exit = raw_input('Enter to exit.')
	if exit == 'show code':
		print str(x)
		raw_input('Enter to exit.')
	quit()

def w_f(a,x):
	a.write(x)
	a.flush()

def soundx():
	winsound.Beep(600,300)

def search(a,b):
	x = 0
	for letter in a:
		if letter == b:
			x += 1
	return x

def findx(x, a_='=', b_='*', c_='\n'):
	i = 0
	b0 = 0
	b1 = 0
	k = 0
	b = []
	z = []
	x = str(x)
	y = int(len(x))
	
	b.append(x.find(a_,0))
	while k == 0:
		b0 = b[i]+1
		i += 1
		b1 = x.find(b_,b0)
		if b1 == -1:
			b1 = x.find(c_,b0)
			b.append(int(b1))
			break
		b.append(int(b1))
	
	k = i - 1
	i = 0
	while i <= k:
		b0 = b[i]+2
		if i < k:
			b1 = b[i+1]-1
		elif k == i:
			b1 = b[i+1]
		z.append(int(x[b0:b1]))
		i += 1

	return z

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

def compare(list):
	i = 0
	list.sort()
	while i != len(list):
		b = list[i]
		a = list.count(b)
		while a != 1:
			del list[i]
			a -= 1
		i += 1
	return list