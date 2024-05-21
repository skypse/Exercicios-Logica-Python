# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Ler dois valores numéricos inteiros e apresentar o resultado da diferença do maior pelo menor valor.

# Programa para calcular a diferença entre 2 números inteiros

# (Saída) - Apresenação
print("Programa que calcula a diferença do maior para o menor")
print()

# (Entrada) - Pedindo dados e armazenando
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# (Processamento) + (Saída) - Verificando a diferença entre eles e calculando
if numero1 > numero2:
    resultado = numero1 - numero2
    print(f'O resultado da diferença do maior para o menor é: {resultado}')
else:
    resultado = numero2 - numero1
    print(f'O resultado da diferença do maior para o menor é: {resultado}')