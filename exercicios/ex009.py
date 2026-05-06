print(f'Quantos doláres eu posso comprar?')
reais = float(input(f'Quantos reais você tem? R$ '))
dol = 4.94
cambio = reais / dol
print(f'Com R${reais:.2f} você pode comprar: US${cambio:.2f}')