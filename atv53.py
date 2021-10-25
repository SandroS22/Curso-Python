frase = str(input('Digite uma frase: ')).lower().join('')
cont = (frase[::-1].lower())
if frase == cont:
    print('A frase é um palindromo!')
if frase != cont:
    print('A frase não é um palindromo!')
