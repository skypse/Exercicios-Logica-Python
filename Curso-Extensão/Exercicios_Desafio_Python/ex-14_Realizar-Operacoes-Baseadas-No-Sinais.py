# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um programa que leia um número e informe se ele é positivo ou negativo.
#            Se for positivo, calcule a raiz quadrada; se for negativo, informe o número ao quadrado.

import math

# leitura do número
numero = float(input("Digite um número: "))

# verificação e operação conforme o sinal do número
if numero > 0:
    print("O número é positivo.")
    raiz_quadrada = math.sqrt(numero)  # calculando a raiz quadrada
    print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}")
elif numero < 0:
    print("O número é negativo.")
    numero_quadrado = numero ** 2  # calculando o quadrado do número
    print(f"O número ao quadrado é {numero_quadrado:.2f}")
else:
    print("O número é zero. Não é nem positivo nem negativo.")
