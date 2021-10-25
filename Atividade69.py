dmaior = 0
homens = 0
mulherdmenor = 0
while True:
    idade = int(input('Insira a idade: '))
    sexo = str(input('Insira o sexo [M/F]: ').upper())
    cont = str(input('Deseja continuar [S/N]? ').upper())
    if idade > 18:
        dmaior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulherdmenor += 1
    if cont == 'N':
        break
print(f'No total temos {dmaior} maior de idade, {homens} homem/ns e {mulherdmenor} mulher(es) com menos de 20 anos.')
print('Processo finalizado.')
