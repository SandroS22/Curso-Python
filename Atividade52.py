num = int(input('Insira um número: '))
if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
    print('O número {}, é um número primo'.format(num))
else:
    print('O número {}, não é um número primo!'.format(num))
