a = open('data\prime\digit_1.txt','r')
c = []
d = 1
i = 0

from definition.factoring import *

while d == 1:
	try:
		part = str(a.next())
	except:
		break
	if part == '0\n' or part == '#\n':
		continue
	c = c + findx(part)
c = compare(c)
print c

raw_input('')



raw_input('')
