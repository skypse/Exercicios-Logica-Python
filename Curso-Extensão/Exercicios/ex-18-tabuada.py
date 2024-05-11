# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Crie um programa que solicite ao usuário um número e imprima a tabuada correspondente até 10.

# Solicite ao usuário um número e imprima a tabuada correspondente até 10

# (Saída) - Apresentação
print("Programa que faz a tabuada com o número que o usuário insere")
print()

# (Entrada) - Pedindo os dados e armazenando
numero = int(input("Digite um número, para ser feito a tabuada: "))
print()

# (Processamento) - Montando a tabuada
for controle in range(1,11):
  tabuada = numero * 1
  print(f"{numero} x {controle} = {tabuada}")