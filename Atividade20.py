import random

a1 = (str(input('Primeiro aluno: ')))
a2 = (str(input('Segundo aluno: ')))
a3 = (str(input('Teceiro aluno: ')))
a4 = (str(input('Quarto aluno: ')))

lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A oredem é {}'.format(lista))
