# Criar uma função chamada soma que solicita 2 valores e exibe o resultado. Chame ela 2 vezes

# Função de somar
def FuncaoSomar():
    print("Programa que faz uma soma\n")
    numero_01 = int(input("Digite o primeiro numero: "))
    print("")
    numero_02 = int(input("Digite o segundo numero: "))
    resultado = numero_01 + numero_02
    print(f"O resultado da sua soma foi:{resultado}\n")
FuncaoSomar()

# Função de subtrair
def FuncaoSubtracao():
    print("Programa que faz uma Subtração\n")
    numero_01 = int(input("Digite o primeiro numero: "))
    print("")
    numero_02 = int(input("Digite o segundo numero: "))

    resultado = numero_01 - numero_02
    print(f"O resultado da sua subtração foi:{resultado}\n")
FuncaoSubtracao()

# Função de dividir
def FuncaoDivisao():
    print("Programa que faz uma Divisão\n")
    numero_01 = int(input("Digite o primeiro numero: "))
    print("")
    numero_02 = int(input("Digite o segundo numero: "))

    resultado = numero_01 / numero_02
    print(f"O resultado da sua divisão foi:{resultado}\n")
FuncaoDivisao()

# Função de multiplicação
def FuncaoMultiplicacao():
    print("Programa que faz uma Multiplicação\n")
    numero_01 = int(input("Digite o primeiro numero: "))
    print("")
    numero_02 = int(input("Digite o segundo numero: "))

    resultado = numero_01 * numero_02
    print(f"O resultado da sua multiplicação foi:{resultado}\n")
FuncaoMultiplicacao()
