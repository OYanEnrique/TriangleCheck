r1=float(input('Enter a number: '))
r2=float(input('Enter a number: '))
r3=float(input('Enter a number: '))

if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
	print('It can form a triangle! ')
	if r1== r2 == r3:
		print('It will form an equilateral triangle')
	elif r1 == r2 or r1 == r3 or r2 == r3:
		print('It will form an isosceles triangle')
	elif r1 != r2 != r3:
		print('It will form an scalene triangle')
else:
	print('It can not form a triangle')