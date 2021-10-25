somaIdade = 0
mediaIdade = 0
maioridadehomem = 0
nomeVelho = ''
totMulher20 = 0
for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1
mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homen mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomeVelho))
print('Ao todo são {} mulheres com menos de de 20 anos'.format(totMulher20))
