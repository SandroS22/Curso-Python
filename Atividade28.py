import random
print('====================\n'
      '|      JOGO        |\n'
      '|       DE         |\n'
      '|   ADIVINHAÇÃO    |\n'
      '====================')

num = random.randint(1, 5)
ans = int(input('Escolha um número de 1 a 5\n'))
if ans == num:
    print('Parabéns você acertou!!!')
else:
    print('Que pena, você errou!O número escolhido foi {}'.format(num))
