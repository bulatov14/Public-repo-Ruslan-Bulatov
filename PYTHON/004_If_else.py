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

name = 'Alex'
if 'm' in name == 'Alex':
    print('My name is Alex')
else:
    print('My name is not Alex')

print('Input pin code')
pin = 1234
userpin = int(input())
if pin == userpin:
    print('How much do you want cash ?')
else:
    print('Input right pin code, you have 2 attempts')
    userpin = int(input())
    if pin == userpin:
        print('How much do you want cash ?')
    else:
        print('Input right pin code, you have only 1 attempt')
        userpin = int(input())
        if pin == userpin:
            print('How much do you want cash ?')
        else:
            print('Your card is blocked')