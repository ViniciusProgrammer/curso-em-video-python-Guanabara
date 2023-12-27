print('{} LOJAS GUANABARA {}'.format(('=' * 10), ('=' * 10)))

valor = float(input('Informe o valor a ser pago: R$ '))
print('''Escolha uma opção de pagamento:
[ 1 ] - Dinheiro/Cheque
[ 2 ] - Avista no cartão
[ 3 ] - 2x no cartão
[ 4 ] - 3x ou mais no cartão''')
escolha = int(input('Informe a sua opção de pagamente: '))

if escolha == 1:
    valor = valor - (valor * 10 /100)
    print('Você pagará pelo produto R$ {:.2f} com 10% de desconto'.format(valor))
elif escolha == 2:
    valor = valor - (valor * 5 / 100)
    print('Você pagará pelo produto R$ {:.2f} com 5% de desconto'.format(valor))
elif escolha == 3:
    parcela = valor / 2
    print('Você pagará o valor total R${:.2f} em 2x de R${:.2f}'.format(valor, parcela))
elif escolha == 4:
    parcelas = int(input('Informe a quantidade parcelas deseja: '))
    if parcelas >= 3:
        acrescimo = valor * (20 /100)
        valor_parcela = (valor + acrescimo) / parcelas
        total = valor_parcela * parcelas
        print('Você pagará um total de R${:.2f} dividido em {}x de R${:.2f}'.format(total, parcelas, valor_parcela))
    else:
        print('Número de parcelas inválida, escolha outra opção de pagamento!')
else:
    print('Opção de pagamento inválida, tente novamente!')
