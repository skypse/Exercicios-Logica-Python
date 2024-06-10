# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: 2) Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer.
# c) Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100).
# d) Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500.

# Item 2) Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer.
numero_tabuada = int(input("Digite um número para calcular sua tabuada: "))

# Apresentação da tabuada
print(f"Tabuada de multiplicação de {numero_tabuada}:")
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

# Item C) Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100).

# Calculando a soma dos cem primeiros números inteiros
soma = sum(range(1, 101))

# Apresentação do resultado
print("Total da soma dos cem primeiros números inteiros:", soma)

# Item D) Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500.

# Variável para armazenar o somatório dos valores pares
soma_pares = 0

for num in range(1, 501):
    # Verifica se o número é par
    if num % 2 == 0:
        # Se for par, adiciona ao somatório
        soma_pares += num

# Somatório dos valores pares
print("Somatório dos valores pares de 1 até 500:", soma_pares)
