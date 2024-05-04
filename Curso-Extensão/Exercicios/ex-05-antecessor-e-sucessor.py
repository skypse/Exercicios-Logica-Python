# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um algoritmo para ler um valor (do teclado) e escrever (na tela) o seu antecessor e sucessor.

# Programa de Antecessor e Sucessor

# (Sáida) - Apresentação
print("Digite um número, que o programa exibe o 'Antecessor' e 'Sucessor'")
print()

# (Entrada)
num1 = int(input('Digite o primeiro número: '))


# (Processamento) Extraindo o 'Antecessor' e 'Sucessor'
antecessor = num1 - 1
sucessor = num1 + 1

# (Saída) Exibindo o resultado do processamento
print('O antecessor do número', num1,'é',antecessor)
print('O sucessor do número', num1,'é',sucessor)
