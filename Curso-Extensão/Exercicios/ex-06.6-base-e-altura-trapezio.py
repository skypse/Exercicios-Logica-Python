# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo, quadrado, triangulo, losango, e trapezio.

# Programa de calculo da área de um 'trapezio'

# (Saída) - Apresentação
print("Programa que calcula área do Trapézio")
print()

# (Entrada) - Pedindo os dados e armazenando
base_maior = float(input("Digite o valor da base maior do trapézio: "))
base_menor = float(input("Digite o valor da base menor do trapézio: "))
altura = float(input("Digite o valor da altura do trapézio: "))

# (Processamento) - Calculando a area
area = (base_maior + base_menor) * altura / 2

# (Saída) - Exibindo os resultados
print("A área do trapézio é:", area)