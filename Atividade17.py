import math
co = float(input('Cateto Oposto:'))
ca = float(input('Cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
