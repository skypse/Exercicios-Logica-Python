# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Ler um valor e escrever se é positivo, negativo ou zero.

# (Saída) - Apresentação
print("Ler um valor e escrever se é positivo, negativo ou zero.")
print()

# (Entrada) - Pedindo o valor e armazenando
valor = int(input("Digite um valor: "))

# (Processamento) - Verificando se o valor é positivo, negativo ou zero
if valor > 0:
  print("O valor é positivo.")
elif valor < 0:
  print("O valor é negativo.")
else:
  print("O valor é zero.")
