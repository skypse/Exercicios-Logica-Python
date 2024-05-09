# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um programa que peça ao usuário para digitar um número e verifique se é positivo, negativo ou zero.

# Peça ao usuário para digitar um número e verifique se é positivo, negativo ou zero

# (Saída) - Apresentação
print("Programa que verifica se o número é positivo, negativo ou neutro")
print()

# (Entrada) - Pedindo dados e armazenando
numero = int(input("Digite um número: "))

# (Processamento) - Efetuando a verificação junto com o processamento de (Saída)
if numero < 0:
  print("Número negativo!")
elif numero == 0:
  print("Número neutro")
else:
  print("Número positivo")