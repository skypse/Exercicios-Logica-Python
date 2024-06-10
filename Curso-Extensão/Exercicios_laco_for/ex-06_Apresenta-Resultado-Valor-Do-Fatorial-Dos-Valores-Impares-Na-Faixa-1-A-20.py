# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: 6) Elaborar um programa que apresente como resultado o valor do fatorial dos valores ímpares situados na faixa numérica de 1 a 10.

# Apresentação
print("Apresentar como resultado o valor do fatorial dos valores ímpares situados na faixa numérica de 1 a 10.")

for num in range(1, 11):
    # Verifica se o número é ímpar
    if num % 2 != 0:
        # Inicializa o fatorial como 1
        fatorial = 1
        # Calcula o fatorial do número ímpar
        for i in range(1, num + 1):
            fatorial *= i
        # Apresenta o resultado
        print(f"O fatorial de {num} é {fatorial}")
