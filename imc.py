peso = float(input('Digite seu peso (kg): '))

altura = float(input('Digite a sua altura(m): '))

imc = float(peso / (altura*altura))

if imc >= 17 and imc < 18.5:
    print('Você esta abaixo do peso!')
    print(f'Seu IMC é equivalente a {imc}')

elif imc > 18.5 and imc <= 25:
    print('Peso ideal!')
    print(f'Seu IMC é equivalente a {imc}')

elif imc >25 and imc <= 30:
    print('Sobrepeso!')
    print(f'Seu IMC é equivalente a {imc}')

elif imc >30 and imc <= 35:
    print('Obesidade!')
    print(f'Seu IMC é equivalente a {imc}')

elif imc >35 and imc <= 40:
    print('Obesidade severa!')
    print(f'Seu IMC é equivalente a {imc:.0f}')


elif imc > 40:
    print('Obesidade mórbita')

    print(f'Seu IMC é equivalente a {imc}')
   



