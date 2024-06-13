# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um programa que leia um número e verifique se ele é maior que 100.
#            Se não for, informe o dobro desse número.

# leitura do número
numero = float(input("Digite um número: "))

# verificação e cálculo
if numero > 100:
    print(f"O número {numero} é maior que 100.")
else:
    dobro = numero * 2
    print(f"O número {numero} não é maior que 100. Seu dobro é {dobro}.")
