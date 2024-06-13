# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um programa que leia dois números inteiros e informe qual deles é o maior.

# leitura dos dois números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# verificação do maior número
if numero1 > numero2:
    print(f"O número {numero1} é maior que o número {numero2}.")
elif numero2 > numero1:
    print(f"O número {numero2} é maior que o número {numero1}.")
else:
    print(f"Os números {numero1} e {numero2} são iguais.")
