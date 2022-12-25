import sys
sys.path.append("../../")
from definition.factoring import *
a = 1
b = 1

while a == 1:
	k = raw_input('do you want to formatting all data? process, digit, both or no?[P/D/B/N]')
	if k == 'B' or k == 'b':
		with open('../process.txt','w') as process:
			process.write('0\n')
		while b <= 10 :
			with open('../prime/digit_%d.txt'%b,'w') as digit:
				digit.write('')
			b += 1
		break
	elif k == 'P' or k == 'p':
		with open('../process.txt','w') as process:
			process.write('0\n')
		break
	if k == 'D' or k == 'd':
		while b <= 10 :
			with open('../prime/digit_%d.txt'%b,'w') as digit:
				digit.write('')
			b += 1
		break
	elif k == 'N' or k == 'n':
		break
	else:
		continue
out()
