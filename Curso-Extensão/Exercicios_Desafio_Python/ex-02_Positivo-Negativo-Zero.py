# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um programa que leia um número inteiro e informe se ele é positivo, negativo ou zero.

# leitura do número inteiro
numero = int(input("Digite um número inteiro: "))

# verificação se o número é positivo, negativo ou zero
if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print(f"O número {numero} é zero.")
