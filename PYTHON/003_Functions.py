var = input()
print(type(var))  # при вводе - любой тип данных (value) становится string всегда

var = int(input())
print(var)  # integer


# функция предназначена для выполнения конкретной задачи - это изолированный блок кода, кот. можно повторно использовать

# функция делает код модульным и компактным, мы можем создавать и свои

# print, type - это функции

# переменная - хранит в себе значение, функция - производит действие и может возвращать инфо

def summ():
    print("hello")

summ()  # hello

num1 = 10
num2 = 20
def summ():
    result = num1 + num2
    print(result)

summ() # 30


def summ(n1, n2):
    result = n1 + n2
    print(result)

summ(10, 20)  # 30

def summ(n1, n2):
    result = n1 + n2
    print(result)

summ('Hello ', 'World_1')  # Hello World_1

def summ(n1, n2):
    result = n1 + n2
    print(result)

summ(n2='World_2', n1='Hello ')  # Hello World_2

def hi(name):
    print('Hello ' + name)

hi('Alex_1')  # Hello Alex_1


def hi(name='Alex_2'):
    print('Hello ' + name)

hi()  # Hello Alex_2

name = 'Alex_3'
def hi(name):
    print('Hello ' + name)

hi(name)  # Hello Alex_3

name = 'Alex_4'
def hi(name, age):
    print('Hello, my name is ' + name + ', I am ' + age)

hi(name, '32')  # Hello my name is Alex_4, I am 32

name = input()
age = input()
def hi(name,age):
    print(name, age)
hi(name,age) # Bob 33

name = 'Alex_5'
age = '32'
def hi(name, age):
    result = name + ' ' + age
    return result

h = hi(name, age) # или print(hi(name, age)) без обьявления переменной h
print (h) # Alex_5 32

var1 = 10  # глобальная переменная
var2 = 20  # глобальная переменная

def summ():
    var3 = 30 # локальная переменная
    var4 = 40 # локальная переменная
    result = var1 + var2
    print(result)

summ() # 10 20 70

var1 = 100  # глобальная переменная
var2 = 20  # глобальная переменная
def summ():
    result = var1 + var2
    print(result)
def sub():
    result = var1 - var2
    print(result)

sub()  # 120 80
