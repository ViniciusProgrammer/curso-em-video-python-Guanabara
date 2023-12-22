distancia = float(input('Informe a distância em Km: '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))

if(distancia <= 200):
    pagamento = distancia * 0.50
    print('Em uma viagem de {:.1f}Km. Você pagará R${:.2f}'.format(distancia, pagamento))
else:
    pagamento = distancia * 0.45
    print('Em uma viagem de {:.1f}Km. Você pagará R${:.2f}'.format(distancia, pagamento))
