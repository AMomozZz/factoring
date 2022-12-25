#Definition
a = 1
z = []
import sys
sys.path.append("..")
from definition.factoring import *

#Prepare read
with open('process.txt','r') as process:
	all_process = str(process.read())
if all_process == '':
	with open('process.txt','a+') as process:
		process.write('0\n')
		process.seek(0,0)
		all_process = str(process.read())

#Read
alllen = countnumber(all_process)
timex = all_process.find('\n',0)
time = int(all_process[0:timex])
print('number of statistics: %d')%time
if all_process[alllen-2:alllen] == '#\n':
	print 'allredy down.'
	out()
elif all_process == '0\n':
	print('No data has been stored.')
	out()
timelen = countnumber(time)

#raw_input('')
#Classify
with open('process.txt','r+') as process:
	while a == 1:
		try:
			part = process.next()
		except:
			break
		if part == '0\n' or part == '#\n':
			continue
		z = z + findx(part)
print z 
#find and delete same number
z = compare(z)
print z

#Prepare finish
back = '\b' * (timelen-1)
output = back + str(time+1)

#Finish
with open('process.txt','a+') as process:
	process.write('#\n')
with open('process.txt','r+') as process:
	process.write('%s'%(output))

print('statistical task %d completed.')%time

#Out
out()