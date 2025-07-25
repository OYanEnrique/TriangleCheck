r1=float(input('Enter a number: '))
r2=float(input('Enter a number: '))
r3=float(input('Enter a number: '))

if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
	print('It can form a triangle! ')
else:
	print('It can not form a triangle')