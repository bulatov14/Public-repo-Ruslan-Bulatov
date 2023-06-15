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
            print('Yuor card is blocked')