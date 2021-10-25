sexo = str(input('Digite seu sexo [M/F]: ')).strip()
while sexo not in 'MmFf':
    print('Insira somente uma das duas opções!!!')
    sexo = str(input('Digite seu sexo [M/F]: ')).strip()
print('Sucesso!')
