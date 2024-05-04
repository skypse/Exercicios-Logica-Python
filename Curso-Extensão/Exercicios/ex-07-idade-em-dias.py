#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

# (Saída) - Apresentação
print("Programa que exibe a idade em dias")
print()
print("Considere 1 ano com 365 dias, e um mês com 30 dias!")
print()

# (Entrada) - Pedindo os dados e armazenando
ano = int(input("Digite quantos anos completos você tem: "))
meses = int(input("Digite quantos meses se passaram após seu último aniversário: "))
dias = int(input("Escreva o dia que está: "))

# (Processamento) - Processando os Calculos
idade = (ano * 365 + meses * 30 + dias)

# (Saída) - Exibindo os resultados do processamento
print("Sua idade em dias é:",idade)