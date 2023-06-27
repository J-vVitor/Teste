valor_do_emprestimo = int(input('Qual o valor do emprestimo?: '))

parcelas= int(input('Quantas parcelas?: '))

valor_da_porcentagem = int(input('Qual o valor da porcentagem?: '))



porcentagem = int((valor_do_emprestimo*valor_da_porcentagem)/100 )

valor = valor_do_emprestimo + porcentagem

resultado = valor/10

print(f' Você vai pagar {parcelas} parcelas de R${resultado:.2f}')


