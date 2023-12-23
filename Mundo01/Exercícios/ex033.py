n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

if n1 > n2 and n1 > n3:
    print('O maior número é {}'.format(n1))
    if n2 > n3:
        print('O menor número é {}'.format(n3))
    else:
        print('O menor número é {}'.format(n2))
elif n2 > n1 and n2 > n3:
    print('O maior número é {}'.format(n2))
    if n1 > n3:
        print('O menor número é {}'.format(n3))
    else:
        print('O menor número é {}'.format(n1))
else:
    print('O maior número é {}'.format(n3))
    if n1 > n2:
        print('O menor número é {}'.format(n2))
    else:
        print('O menor número é {}'.format(n1))
