while True:
    resp = int(input('Quer ver a tabuada de qual número? '))
    if resp < 0:
        break
    print('=' * 12)
    print(f'{resp} x 1 = {resp * 1}\n'
          f'{resp} x 2 = {resp * 2}\n'
          f'{resp} x 3 = {resp * 3}\n'
          f'{resp} x 4 = {resp * 4}\n'
          f'{resp} x 5 = {resp * 5}\n'
          f'{resp} x 6 = {resp * 6}\n'
          f'{resp} x 7 = {resp * 7}\n'
          f'{resp} x 8 = {resp * 8}\n'
          f'{resp} x 9 = {resp * 9}\n'
          f'{resp} x 10 = {resp * 10}')
    print('=' * 12)
print('Até mais!')
