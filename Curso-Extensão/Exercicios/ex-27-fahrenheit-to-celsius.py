# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula C= (F - 32)*5/9.):

# (Saída) - Apresentação
print("Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius.")
print()

# (Entrada) - Pedindo dados e armazenando
fahrenheit = int(input("Digite sua temperatura em graus Fahrenheit: "))
print()

# (Processamento) - efetuando a conversão
celsius = (fahrenheit - 32) * 5/9

# (Saída) - Apresentando resultados
print(f"Sua temperatura em celsius ficou {celsius}º")