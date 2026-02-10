# nome = input('Qual é o seu nome? ')
# print(f'Prazer em te conhecer {nome}!')
# print(f'Olá, {nome:=^20}')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma vale {s}, o produto vale {m} e a divisão vale {d:.3f}.') # end=' ' , \n 
print(f'Divisão inteira: {di}. Potência: {e}.')