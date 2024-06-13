# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um programa que leia o código de um produto e informe a sua categoria:
#            1 a 10: Alimento não-perecível
#            11 a 20: Alimento perecível
#            21 a 30: Vestuário
#            31 a 40: Eletrônicos
#            Outros: Código inválido

# leitura do código do produto
codigo = int(input("Digite o código do produto: "))

# determinação da categoria do produto
if codigo >= 1 and codigo <= 10:
    print("Categoria: Alimento não-perecível")
elif codigo >= 11 and codigo <= 20:
    print("Categoria: Alimento perecível")
elif codigo >= 21 and codigo <= 30:
    print("Categoria: Vestuário")
elif codigo >= 31 and codigo <= 40:
    print("Categoria: Eletrônicos")
else:
    print("Código inválido")
