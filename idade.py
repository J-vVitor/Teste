ano_de_nascimento = int(input('Em que ano você nasceu?: '))

ano_atual = int(input('Qual o ano atual?: '))

idade = ano_atual - ano_de_nascimento

if idade >=0 and idade <=17:
    print(f' Você tem {idade} anos. Você é jovem')

elif idade >=18 and idade <=49:
     print(f'Você tem {idade} anos. Você é maduro')

else:
    print(f'Você tem {idade} anos. Você é idoso')
