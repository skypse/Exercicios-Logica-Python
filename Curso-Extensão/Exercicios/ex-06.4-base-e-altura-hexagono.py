# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo, quadrado, triangulo, losango, e trapezio.

# Programa de calculo da área de um 'hexagono'

import math

# (Saída) - Apresenação
print("Programa que calcula área do hexagono")
print()

# (Entrada) - Pedindo os dados e armazenando
lado = float(input("Insira o comprimento do lado do hexágono: "))

# (Processamento) - Fazendo o calculo da area de um hexagono
area = (3 * math.sqrt(3) * lado ** 2) / 2

# (Saída) - Exbindo resultados
print("A área do hexágono é",area)
