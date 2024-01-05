## Minha solução ##
cedulas50 = 50
cedulas20 = 20
cedulas10 = 10
cedulas1 = 1
valor = int(input('Informe um valor: %RS'))
cedulas50 = valor // 50
resto50 = valor % 50
cedulas20 = resto50 // 20
resto20 = resto50 % 20
cedulas10 = resto20 // 10
resto10 = resto20 % 10
cedulas1 = resto10 // 1
resto1 = resto10 % 1
print(f'Com o valor {valor} você pode sacar: \n{cedulas50} cédulas de R$50,00 \n{cedulas20} cédulas de R$20,00 \n{cedulas10} cédulas de R$10,00 \n{cedulas1} cédulas de R$1,00')

'''
saque = int(input('Digite o valor que deseja sacar: R$ '))
n50 = n20 = n10 = n1 = 0
while True:
    if saque >= 50:
        saque -= 50
        n50 += 1
    else:
        if saque >= 20:
            saque -= 20
            n20 += 1
        else:
            if saque >= 10:
                saque -= 10
                n10 += 1
            else:
                if saque >= 1:
                    saque -= 1
                    n1 += 1
    if saque == 0:
        break
print(f'Você receberá {n50} notas de 50, {n20} de 20, {n10} de 10 e {n1} de 1.')
'''