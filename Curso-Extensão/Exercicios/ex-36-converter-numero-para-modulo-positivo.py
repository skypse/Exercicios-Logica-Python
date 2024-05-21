# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Efetuar a leitura de um valor inteiro positivo ou negativo e apresentar o número lido como sendo um valor positivo, ou seja, o programa deverá apresentar o módulo de um número fornecido. Lembre-se de verificar se o número fornecido é menor que zero; sendo, multiplique-o por -1.


# (Saída) - Apresenação
print("Programa que converte número para modulo positivo")
print()

# (Entrada) - Pedindo dados e armazenando
numero = int(input("Digite um número: "))

# (Processamento) + (Saída) - verificando e exibindo
if numero < 0:
    resultado = numero * -1
    print(f'O número digitado foi transformado em positvo: {resultado}')
else:
    print(f'O número digitado já é positivo')