# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Faça um programa que receba um número inteiro e retorne se é primo ou não

# Receba um número inteiro e retorne se é primo ou não

# (Saída) - Apresentação
print("Programa que recebe um número inteiro e retorne se é primo ou não")
print()

# (Entrada) - Pedindo dados e armazenando
numero = int(input("Digite um número: "))

# (Processamento) - Efetuando a verificação

  # números que são menores que 2 não são primos
def verifica_primo(numero):
    if numero < 2:
        return False
    # verifica se o número é divisível apenas por 1 e ele mesmo
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

if verifica_primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")