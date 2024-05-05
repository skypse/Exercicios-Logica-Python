# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Faça um programa que pergunte ao usuário o valor do produto e o percentual de desconto, e retorne o valor final após o desconto.

# Programa para calcular o valor final de um produto após aplicar um desconto

# (Saída) - Apresentação
print("Programa para calcular o valor final de um produto após aplicar um desconto")
print()

# (Entrada) - Pedindo dados e armazenando
valor_produto = float(input("Digite o valor do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

# (Processamento) - Fazendo o cálculo
desconto = valor_produto * (percentual_desconto / 100)
valor_final = valor_produto - desconto

# (Saída) - Exibindo o resultado
print("O valor final do produto após aplicar um desconto de", percentual_desconto, "% é:", valor_final)
