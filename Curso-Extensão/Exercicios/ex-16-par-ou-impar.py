# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Par ou ímpar

# Programa para checar se um número é par ou ímpar

# (Saída) - Apresentação
print("Programa que verifica se é par ou ímpar")
print()

# (Entrada) - Pedindo um número e armazenando
num1 = int(input("Digite um número: "))

# (Processamento) - Verificando se o número é par ou ímpar
if num1 % 2 == 0:
    # (Saída) - Exibindo resultados
    print("O número digitado é Par!")
else:
    # (Saída) - Exibindo resultados
    print("O número digitado é ímpar!")
