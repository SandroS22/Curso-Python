salario = float(input('Quanto vc recebe? '))
aum10 = (salario * (10/100)) + salario
aum15 = (salario * (15/100)) + salario

if salario >= 1250.00:
    print('Vc receberá {}'.format(aum10))
else:
    print('Vc receberá {}'.format(aum15))
