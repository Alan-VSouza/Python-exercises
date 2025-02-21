#Sabe-se que uma lata de tinta tem um custo C e é capaz de pintar uma área de M metros quadrados. Faça um programa que leia a largura L, a altura A de uma parede, o valor C de uma lata de tinta e o rendimento M desta lata. Após isso, imprima quantas latas de tintas são necessárias e o custo total (com duas casas decimais). Assuma que não é possível comprar lata de tinta fracionada.

import math

L = float(input())
A = float(input())
C = float(input())
M = float(input())

area = L * A
rendimento = area / M
latas = math.ceil(rendimento)
print(f'{latas:.0f}')
valor = latas * C

print(f'{valor:.2f}')