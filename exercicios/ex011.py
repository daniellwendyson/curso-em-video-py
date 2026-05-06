produto = float(input(f'Digite o preço do produto: R$ '))
desconto = float(input(f'Digite o valor do desconto: '))
c = produto * (desconto / 100)
final = produto - c 
print(f'Valor do produto com {desconto:.0f}% de desconto é R$ {final:.2f}')