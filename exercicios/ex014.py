print(f'===== Aluguel de carros =====')
dias = int(input(f'Quantos dias alugados? '))
km = float(input(f'Quantos Km rodados? '))
vdias = dias * 60 
vkm = km * 0.15
valorfinal = vdias + vkm 
print(f'O total a pagar é de R${valorfinal:.2f}')
