str1 = 'hello'
print(dir(str1))		#выводит все возможные команды


str1 = 'hello'
print(str1.upper())		#все буквы капс локом


a = 'Alex'
b = 'Hello {}'
result = b.format(a)
print(result)			#Hello Alex


name = 'Alex'
surname = 'Orlov'
a = '{} {}'
result = a.format(name, surname)
print(result)							#Alex Orlov


name = 'Alex'
surname = 'Orlov'
result = f'{name} {surname}'
print(result)							#f string нотация


a = input()
print(a)			#в input по дефолту - строковый тип данных


a = int(input())
print(type(a))			#<class 'int'>