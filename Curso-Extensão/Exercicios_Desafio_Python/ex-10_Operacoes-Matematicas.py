# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um programa que leia dois números e uma operação (adição, subtração, multiplicação ou divisão)
#            e realize a operação correspondente.

# leitura dos dois números e da operação
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
operacao = input(
    "Digite a operação desejada (+ para adição, - para subtração, * para multiplicação, / para divisão): ")

# realização da operação
if operacao == '+':
    resultado = numero1 + numero2
    operacao_texto = "adição"
elif operacao == '-':
    resultado = numero1 - numero2
    operacao_texto = "subtração"
elif operacao == '*':
    resultado = numero1 * numero2
    operacao_texto = "multiplicação"
elif operacao == '/':
    # verificação para evitar divisão por zero
    if numero2 != 0:
        resultado = numero1 / numero2
        operacao_texto = "divisão"
    else:
        print("divisão por zero não permitida.")
        resultado = None  # definição do none
        operacao_texto = "operação inválida"
else:
    print("Operação inválida.")
    resultado = None  # definição do none
    operacao_texto = "operação inválida"

# resultado da operação
if resultado is not None:
    print(f"Resultado da {operacao_texto}: {resultado}")
