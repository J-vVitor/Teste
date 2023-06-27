mae = float(input('Valor: '))
pai = float(input('Valor: '))
filho = float(input('Valor: '))

resultado = mae + pai + filho

print(f'Total: R${resultado :.2F}')

if resultado >=10000:
    print('Partiu Disney!')

elif resultado >=5000 and resultado < 10000:
    print('Visitar a familia')

else:
    print('Ficar em casa')