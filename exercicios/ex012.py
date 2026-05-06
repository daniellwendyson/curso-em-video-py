salario = float(input(f'Qual o salário do funcionário? '))
aumento = float(input(f'Qual a porcentagem de aumento? '))
c = aumento / 100
a = salario * c 
novosalario = salario + a 
print(f'Seu novo salário é: R${novosalario:.2f}')