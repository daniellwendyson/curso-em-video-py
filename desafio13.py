produto = float(input('Digite o preço do produto: '))
desconto = int(input('Digite a porcentagem de desconto: '))
c = produto * (desconto / 100)
final = produto - c
print(f'Valor do produto com {desconto}% de desconto: {final}')