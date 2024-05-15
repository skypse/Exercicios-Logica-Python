# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito.
# Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito).
# Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
# senão escrever a mensagem 'Saldo Negativo'.

# (Saída) - Apresentação
print("Calcular o saldo atual e verificar se é positivo ou negativo.")
print()

# (Entrada) - Pedindo dados e armazenando
numero_conta = int(input("Digite o número da conta do cliente: "))
saldo = float(input("Digite o saldo: "))
debito = float(input("Digite o débito da conta: "))
credito = float(input("Digite o crédito da conta: "))

# (Processamento) - Calculando o saldo atual
saldo_atual = saldo - debito + credito

# (Saída) - Exibindo o saldo atual e verificando se é positivo ou negativo
if saldo_atual >= 0:
    print("Saldo Positivo")
    print()
    print(f"Saldo atual é: R${saldo_atual}")
else:
    print("Saldo Negativo")
    print()
    print(f"Saldo atual é: R${saldo_atual}")
