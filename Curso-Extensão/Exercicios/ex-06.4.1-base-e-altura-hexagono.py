# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo, quadrado, triangulo, losango, e trapezio.

# Programa de calculo da área de um 'hexagono'

import math

# (Saída) - Apresentação
print("Programa que calcula área de um hexagono")
print()

# (Entrada) - Pedindo dados e apresentando
lado = float(input("Digite o valor do lado de um hexagono para calcular sua área: "))
print()

# (Processamento) - Efetuando os calculos
resultado = ((3 * pow(lado,2) * math.sqrt(3)) / 2)

# (Saída) - Apresentando o resultado
print("O calculo da área deu:",round(resultado,2),"m²")