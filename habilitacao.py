ano_de_nascimento  = int(input('Qual ano você nasceu?: '))
ano_atual  = int(input('Ano atual?: '))

idade = int(ano_atual- ano_de_nascimento)

if idade >= 18:
    print(f' Você tem {idade} anos,você está apto para tirar habilitação')

else:
    print(f' Você tem {idade} anos,você  ainda não tem a idade minima pra tirar habilitação')