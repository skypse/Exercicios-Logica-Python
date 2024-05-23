# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Efetuar a leitura de três valores (variáveis A, B e C) e apresentá-los dispostos em ordem crescente.

# (Saída) - Apresentação
print("Programa que efetua a leitura de 3 valores, e apresenta em ordem crescente")
print()

# (Entrada) - Pedindo os dados e armazenando
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

# (Processamento) - Apresentando em ordem crescente
valores = [valor1, valor2, valor3]

valores_ordenados = sorted(valores)

# (Saída) - Exibir mensagem
print("Os valores em ordem crescente são:",valores_ordenados)