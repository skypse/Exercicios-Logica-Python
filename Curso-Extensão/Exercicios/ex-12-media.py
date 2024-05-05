# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Crie um programa que pergunte ao usuário a quantidade de dias, horas, minutos e segundos, e calcule o total em segundos.

# Programa para calcular o total em segundos a partir de dias, horas, minutos e segundos

# (Saída) - Apresentação
print("Programa para calcular o total em segundos")
print()

# (Entrada) - Pedindo dados e armazenando
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

# (Processamento) - Calculando o total em segundos
total_segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

# (Saída) - Exibindo o total em segundos
print("O total em segundos é:", total_segundos)
