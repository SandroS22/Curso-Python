term = int(input('Qual o primeiro termo? '))
raz = int(input('Digite a razão: '))
n = 1
while n <= 10:
    print('{} -> '.format(term), end='')
    term += raz
    n += 1
print('FIM!!!')
