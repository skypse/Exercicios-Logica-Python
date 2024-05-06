# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Faça um programa que receba a idade do usuário e imprima se ele é maior de idade ou não.

# (Saída) - Apresentação
print("Programa que verifica se o usuário é de maior")
print()

# (Entrada) - Pedindo dados e armazenando
nome = input("Qual o seu nome?: ")
idade = int(input("Qual sua idade?: "))

# (Processamento) - Faz a verificação se o usuário é de maior
if (idade > 18):
    # (Saída) - Exibindo resultados
    print(nome+", você já é de maior!")
else:
    # (Saída) - Exibindo resultados
    print(nome+", você não é de maior!")