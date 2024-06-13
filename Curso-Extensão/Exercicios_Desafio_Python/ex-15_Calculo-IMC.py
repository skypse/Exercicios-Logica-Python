# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um programa que leia o peso e a altura de uma pessoa, calcule o IMC e informe a categoria:
#            Abaixo do peso: IMC < 18.5
#            Peso normal: 18.5 <= IMC < 24.9
#            Sobrepeso: 25 <= IMC < 29.9
#            Obesidade grau I: 30 <= IMC < 34.9
#            Obesidade grau II: 35 <= IMC < 39.9
#            Obesidade grau III: IMC >= 40

# leitura do peso e altura
peso = float(input("Digite o peso da pessoa (em kg): "))
altura = float(input("Digite a altura da pessoa (em metros): "))

# cálculo do IMC
imc = peso / (altura ** 2)

# determinação da categoria do IMC
if imc < 18.5:
    categoria = "Abaixo do peso"
elif imc < 24.9:
    categoria = "Peso normal"
elif imc < 29.9:
    categoria = "Sobrepeso"
elif imc < 34.9:
    categoria = "Obesidade grau I"
elif imc < 39.9:
    categoria = "Obesidade grau II"
else:
    categoria = "Obesidade grau III"

# exibição do resultado
print(f"O IMC calculado é: {imc:.2f}")
print(f"Categoria: {categoria}")
