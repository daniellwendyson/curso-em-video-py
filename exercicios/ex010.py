largura = float(input(f'Qual a largura da parede? '))
altura = float(input(f'Qual a altura da parede? '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem uma dimensão de {largura:.2f}x{altura:.2f} e sua área é de {area:.3f}m²')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}l de tinta.')