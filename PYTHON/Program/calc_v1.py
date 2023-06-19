
what = input('Input "+" or "-" : ')

a = float(input('Input number: '))
b = float(input('Input number: '))

if what == '+':
    d = a + b
    print('Result: ' + str(d))
elif what == '-':
    d = a - b
    print('Result: ' + str(d))
else:
    print('You choose wrong operation')