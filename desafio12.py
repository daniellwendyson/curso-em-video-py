largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura 
tinta = area / 2
print(f'A área da parede é: {area}')
print(f'Sabendo que a cada litro de tinta pinta uma área de 2m², a quantidade necessária para pintar a parede são de {tinta} litros.')