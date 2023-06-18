# a = int(input('Input 1 value: '))
# b = int(input('Input 2 value: '))
# result = a/b
# print(result)       # 6.666666667

# a = int(input('Input 1 value: '))
# b = int(input('Input 2 value: '))
# result = int(a/b)
# print('Result: ' + str(result))       # 6

# a = int(input('Input 1 value: '))
# b = int(input('Input 2 value: '))
# try:
#     result = a/b
# except ZeroDivisionError:
#     print('на 0 делить нельзя')
# print(result)

a = int(input('Input 1 value: '))
b = int(input('Input 2 value: '))
try:
    result = a/b
except ZeroDivisionError:
    result = 0
    print('на 0 делить нельзя')
print(result)

result_2 = a + b
print(result_2)     # если мы знаем что где то может быть ошибка, то можно юзать try/except которая отловит ошибку и код мог работать дальше