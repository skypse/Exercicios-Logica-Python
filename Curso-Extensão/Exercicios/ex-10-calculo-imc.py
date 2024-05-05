# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Crie um programa que solicite ao usuário sua altura e peso, e calcule seu índice de massa corporal (IMC).

# Programa para calcular o índice de massa corporal (IMC)

# (Saída) - Apresenação
print("Programa que calcula o IMC")
print()

# (Entrada) - Pedindo dados e armazenando
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))

# (Processamento) - Fazendo o calculo
imc = peso / (altura ** 2)

# (Saída) - Exibindo o resultados
print("Seu índice de massa corporal (IMC) é:", imc)
