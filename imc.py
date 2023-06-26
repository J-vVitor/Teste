peso = float(input('Digite seu peso (kg): '))

altura = float(input('Digite a sua altura(m): '))

imc = float(peso / (altura*altura))

if imc >= 18.6 and imc <= 25:
    print('Você está com o peso ideal!')

else:
    print('Você está com o peso desregulado!')

print(f'Seu IMC é equivalente a {imc}')



