from random import randint
print('====================\n'
      '|      JOGO        |\n'
      '|       DA         |\n'
      '|   ADIVINHAÇÃO    |\n'
      '====================')

vida = 2
num = randint(1, 5)
print(num)
ans = int(input('Escolha um número de 1 a 5\n'))
while ans != num:
    print('Você errou.Tente novamente!')
    ans = int(input('Escolha um número de 1 a 5\n'))
    if ans == num:
        print('Você acertou')
    else:
        vida = vida - 1
    if vida == 0:
        print('Suas chances acabaram!')
        break
