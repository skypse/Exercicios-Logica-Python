# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: 3) Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500.

# Apresentação Programa
print("Programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500")

# Processamento
numero = 1
contadora = 0

while numero <= 500:
    if (numero % 2 == 0):
        contadora += numero
    numero += 1

print(contadora)
