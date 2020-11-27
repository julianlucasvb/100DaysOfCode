valor = float(input('Quanto de dinheiro você possui? R$'))
dolar = valor / 5.34
euro = valor / 6.36
print('Com o valor de R${:.2f} que você possui você pode comprar US${:.2f} dolares!'.format(valor, dolar))
print('Com o valor de R${:.2f} que você possui você pode comprar €{:.2f} euros!'.format(valor, euro))