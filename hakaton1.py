'''
1 problem
products = ["яблоко", "груша", "арбуз", "банан", "мандарин"]
print(products)
a =int(input('Add your index: '))

if a > 4:
	print('invalid index')
else:
	products.pop(a)
	print(products)
problem 2

points = 0
print('Your points:', points)
print('Choose your version:\n1)3+8. 2)7+3. 3)6+7.')
ques1 = int(input('Where is 10: '))
if ques1 == 2:
	points +=1
	print('Right!', points)
else:
	print('Not right')
print('Choose your version:\n1)12+26. 2)30+12. 3)15+12.')
ques2 = int(input('Where is 42: '))
if ques2 == 2:
	points +=1
	print('Rught!', points)
else:
	print('Not right')
print('Choose your version:\n1)100+120. 2)300-100. 3)150+120.')
ques3 = int(input('Where is 220: '))
if ques3 == 1:
	points += 1
	print('Right!', points)
else:
	print('Not right')
print('Your total point:',points)

if points == 3:
	print('Отлично')
elif points == 2:
	print('good')
else:
	print('Fail')
problem3

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = int(input('Add your number from 1 to 9: '))
print(a[b:])
'''

