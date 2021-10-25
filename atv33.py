a = int(input('Primerio valor: '))
b = int(input('Segundo valor: '))
c = int(input('Segundo valor: '))

maior = a
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
