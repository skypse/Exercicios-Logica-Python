# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Crie um programa que solicite o raio de um círculo e calcule sua área.

import math

# Programa para calcular a área de um círculo

# (Saída) - Apresentação
print("Programa para calcular a área de um círculo")
print()

# (Entrada) - Pedindo o raio e armazenando
raio = float(input("Digite o raio do círculo: "))

# (Processamento) - Calculando a área
area = math.pi * (raio ** 2)

# (Saída) - Exibindo a área
print("A área do círculo é:", area)
