dis = int(input('Qual a distância percorrida? '))
multap = dis * 0.50
multag = dis * 0.45

if dis <= 200:
    print('O valor a ser pago é R${}'.format(multap))
else:
    print('O valor a ser pago é R${}'.format(multag))
