barato = ''
menor = cont = maiorMil = total = 0
while True:
    produto = str(input('Nome: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        maiorMil += 1
    if cont == 1 or preco < menor:
        barato = produto
        menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de produtos com valor maior que R$1000.00: {maiorMil}')
print(f'O produto mais barato foi {barato} e seu valor é de {menor}')
print(f'O total gasto foi de {total}')
