from random import randint
num = 0
result = 0
finalresult = str('')
vitorias = 0
while True:
    esco = str(input('Impar ou par? ').upper())
    num = int(input('Escolha um número de 0 a 10: '))
    oponente = randint(0, 11)
    resultado = num + oponente
    if resultado % 2 == 0:
        finalresult = 'Par'.upper()
    if resultado % 2 == 1:
        finalresult = 'Impar'.upper()
    if esco == 'PAR' and finalresult == 'PAR' or esco == 'IMPAR' and finalresult == 'IMPAR':
        print(f'Você escolheu {num} e o computador {oponente}. Total deu {resultado} DEU {finalresult}')
        print('Você venceu!!!')
        vitorias += 1
    else:
        print(f'Você escolheu {num} e o computador {oponente}. Total deu {resultado} DEU {finalresult}')
        print('Voccê perdeu.')
        print(f'Você obteve {vitorias} vitória(s) consecutiva(s).')
        break
