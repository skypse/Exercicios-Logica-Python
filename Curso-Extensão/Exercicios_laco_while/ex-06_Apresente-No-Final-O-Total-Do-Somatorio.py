# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: 6) Elaborar um programa que efetue a leitura de 10 valores numéricos
#  e apresente no final o total do somatório e a média aritmética dos valores lidos.

# Apresentação do Programa
print("Leitura de 10 valores numéricos e cálculo do somatório e da média aritmética")

# variaveis
soma = 0
contador = 0
quantidade = 10

# Processamento
while contador < quantidade:
    valor = float(input(f"Digite o valor {contador + 1}: "))
    soma += valor
    contador += 1

# Cálculo da média
media = soma / quantidade

# Resultados
print(f"\nTotal do somatório: {soma}")
print(f"Média aritmética: {media}")
