# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um programa que leia um número e verifique se ele está no intervalo de 10 a 20 (inclusive).

# leitura do número
numero = float(input("Digite um número: "))

# verificação se o número está no intervalo de 10 a 20
if numero >= 10 and numero <= 20:
    print(f"O número {numero} está no intervalo de 10 a 20.")
else:
    print(f"O número {numero} não está no intervalo de 10 a 20.")
