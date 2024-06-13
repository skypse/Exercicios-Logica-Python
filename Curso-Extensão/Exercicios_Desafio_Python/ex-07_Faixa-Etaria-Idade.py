# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um programa que leia a idade de uma pessoa e informe se ela é uma criança (0-12 anos),
#            adolescente (13-17 anos), adulto (18-59 anos) ou idoso (60 anos ou mais).

# leitura da idade
idade = int(input("Digite a idade da pessoa: "))

# verificação da faixa etária
if idade >= 0 and idade <= 12:
    print("A pessoa é uma criança.")
elif idade >= 13 and idade <= 17:
    print("A pessoa é um adolescente.")
elif idade >= 18 and idade <= 59:
    print("A pessoa é um adulto.")
elif idade >= 60:
    print("A pessoa é um idoso.")
else:
    print("Idade digitada inválida.")
