n1 = int(input('Insira primeiro valor: '))
n2 = int(input('Insira segundo valor: '))
opcao = 0
while opcao != 5:
    print('[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos números \n[5]Sair do programa')
    opcao = int(input('Qual sua escolha? '))
    if opcao == 1:
        soma = n1 + n2
        print('{} + {} = {}\n'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('{} x {} = {}\n'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número é {}\n'.format(maior))
    elif opcao == 4:
        print('Insira os valores')
        n1 = int(input('Insira um valor: '))
        n2 = int(input('Insira outro valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Por favor insira somente os números válidos!\n')
