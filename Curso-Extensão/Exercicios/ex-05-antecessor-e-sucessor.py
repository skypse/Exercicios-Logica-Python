# (Saída) Programa que exibe o seu antecessor e sucessor

print("Digite um número, que o programa exibe o 'Antecessor' e 'Sucessor'")
print()

# (Entrada)
num1 = int(input('Digite o primeiro número: '))


# (Processamento) Extraindo o 'Antecessor' e 'Sucessor'
antecessor = num1 - 1
sucessor = num1 + 1

# (Saída) Exibindo o resultado do processamento
print('O antecessor do número', num1,'é',antecessor)
print('O sucessor do número', num1,'é',sucessor)
