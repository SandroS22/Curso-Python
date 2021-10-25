term = int(input('Qual o primeiro termo? '))
raz = int(input('Digite a razão: '))
n = term + (10 - 1) * raz
for i in range(term, n + raz, raz):
    print('{}'.format(i), end=' ')
