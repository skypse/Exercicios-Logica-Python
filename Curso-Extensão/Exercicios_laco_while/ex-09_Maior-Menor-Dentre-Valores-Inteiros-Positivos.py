# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: 9) Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo seja informado.
# Ao final devem ser apresentados o maior e o menor valores informados pelo usuário.

# Apresentação do Programa
print("Programa para encontrar o maior e o menor valor dentre valores inteiros positivos")

# Varaveis
maior_valor = float('-inf')  # Menor valor
menor_valor = float('inf')   # Maior valor

# Processamento
while True:
    valor = int(
        input("Digite um valor positivo (ou um valor negativo para encerrar): "))

    # Verifica se o valor é negativo
    if valor < 0:
        break

    # Atualiza o maior e o menor valor, se necessário
    if valor > maior_valor:
        maior_valor = valor
    if valor < menor_valor:
        menor_valor = valor

# Apresentação dos resultados
if not (maior_valor == float('-inf') and menor_valor == float('inf')):
    print(f"O maior valor informado foi: {maior_valor}")
    print(f"O menor valor informado foi: {menor_valor}")
else:
    print("Nenhum valor positivo foi informado.")
