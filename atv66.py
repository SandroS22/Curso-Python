num = 0
cont = 0
soma = 0
while True:
    num = int(input('Digite um valor! 999 para interromper: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'O total de números foi {cont} e a soma {soma}!')
