from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    nasc = int(input('Em que ano a {}ª nasceu? '.format(i)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E teambém tivemos {} pessoas menores de idade'.format(totmenor))
