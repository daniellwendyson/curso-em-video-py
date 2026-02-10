salario = float(input('Qual o salário do funcionário? '))
aumento = float(input('Qual a porcentagem de aumento? '))
c = aumento / 100
a = salario * c 
novosalario = salario + a 
print(f'Seu novo salário é: R$ {novosalario}')