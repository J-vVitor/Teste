pn = float(input('Primeira nota: '))
sn = float(input('Segunda nota: '))
m = int(7)

resultado = (pn + sn)/2
 
if resultado >= 7:
    print(f'Média: {resultado}')
    print('Aluno: Aprovado')

elif resultado > 5 and resultado < 7:
    print(f'Média {resultado}')
    print('Aluno: Recuperação')

else:
    print(f'Média {resultado}')
    print('Aluno: Reprovado')