# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário escrever NÃO É MAIOR QUE 10!

# (Saída) - Apresentação
print("Programa que fala se um número é maior que 10")
print()

# (Entrada) - Pedindo os dados e armazenando
numero = int(input("Digite um número: "))

# (Processamento) - Aplicando a lógica para efetuar a saída
if numero > 10:
    # SE numero maior que 10 = print abaixo
    print(f"{numero} é maior que 10")
elif numero == 10:
    # SE número igual a 10 = print abaixo
    print(f"{numero} é igual à 10")
else:
    # SE número não é maior, nem igual, automaticamente é menor!
    print(f"{numero} é menor que 10")