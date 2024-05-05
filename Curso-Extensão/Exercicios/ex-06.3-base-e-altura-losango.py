# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo, quadrado, triangulo, losango, e trapezio.

# Programa de calculo da área de um 'losango'

# (Saída) - Apresenação
print("Programa que calcula área do losango")
print()

# (Entrada) - Pedindo os dados e armazenando
diagonal_maior = int(input('Digite a diagonal maior: '))
diagonal_menor = int(input('Digite a diagonal menor: '))

# (Processamento) - Fazendo o calculo da área do losango
calculo = diagonal_maior * diagonal_menor / 2

# (Saída) - Exibindo o resultado dos calculos
print("A área do losango é: ",calculo)