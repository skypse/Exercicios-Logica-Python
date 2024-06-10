# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: 7) Elaborar um programa que apresente os resultados da soma e da média aritmética dos valores pares
# situados na faixa numérica de 50 a 70.

# Apresentação do Programa
print("Soma e média aritmética dos valores pares na faixa de 50 a 70")

# variaveis
soma = 0
contador = 0
numero = 50

# Processamento dos valores
while numero <= 70:
    if numero % 2 == 0:  # Verifica se o número é par
        soma += numero
        contador += 1
    numero += 1

# Cálculo da média
media = soma / contador if contador != 0 else 0

# Resultados
print(f"Soma dos valores pares: {soma}")
print(f"Média aritmética dos valores pares: {media:.2f}")
