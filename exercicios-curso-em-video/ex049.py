num = int(input('Escolha um número para tabuada: '))
for c in range(1, 11):
    print('{} X {} = {}'.format(num, c, (num * c)))
