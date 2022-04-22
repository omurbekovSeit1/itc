'''
0 problem
a = [(Axe), (Slark), (Luna), (Bane), (Mirana)]

1 problem
a = ('AK', 'M4', 'AWP')
print(a)
print(a[0])
print(a[1])
print(a[2])

2 problem

a = [1, 'Leo', 2.5, ('Vasya'), True]

3 problem

a = ['leo ', 'Seku ', 'Kani ','Aske ', 'Adyl ']

print(''.join(a))

4 problem

a = [1, 2, 3]
b = [4, 5, 6]

print(a)
a.extend(b)
print(a)

5 problem

a = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jackson', 'Jhon',
 'Jack', 'Jimmy', 'Jackson', 'Jhon'] 
b = a.count('Jack')
print(b)

6 problem

a = ['Jack', 'Jimmy', 'Jackson', 'Jhon']

a.remove('Jack')
print(a)

7 problem

a = []
a.append('Seit')
print(a)
a.append('2002')
print(a)
a.append('Python')
print(a)

8 problem

a = ['int', 'str', 'bool', 'if', 'else', 'elif', 'loop', 'tuple', 'list', 'None', True, False]
print(a.index('loop'))
a.pop(6)
print(a)

9 problem

Num = [0, 2, 4, 7, 1, 8, 0, -3, 7, 0, -2, 4, 0, 


mini Hakatonchik

users = []
login =str(input('Add your login: '))
password1 =str(input('Add your password: '))
password2 = input('Add your password 1 more time: ')
if not login.isdigit() and not login.isalpha():
	print('OK')
	if password1 == password2:
		print('Password is right')
		users.append((login,password1))
		print('Login saved')
		print('Password saved')
		print(users)
	else:
		print("Your password is different")
else:
	print('Invlid login(exemple:Seku2002)')

'''

