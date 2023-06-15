def summ():
	print("hello")
summ()					#hello


def summ(n1, n2):
    result = n1 +n2
    print(result)
summ(10,20)				#30


def summ(n1, n2):
    result = n1 +n2
    print(result)
summ(n2 = 'World', n1 = 'Hello')		#HelloWorld


def hi(name = 'Alex'):
    print('Hello ' + name)
hi()									#Hello Alex


var1 = 100 #глобальная переменная
var2 = 20 #глобальная переменная
def summ():
    result = var1 + var2
    print(result)
summ()
def sub():
    result = var1 - var2
    print(result)
sub()									#120 80

age = 25
if age == 25:
    print('I am 25')
else:
    print('I am not 25')  # I am 25

age = 24
if age == 25:
    print('I am 25')
elif age > 25:
    print('I am more 25')
else:
    print('I am not 25')  # I am not 25