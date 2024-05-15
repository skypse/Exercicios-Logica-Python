# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.

# (Saída) - Apresentação
print("Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.")
print()

# (Entrada) - Pedindo dados e armazenando
salario_mensal = float(input("Digite seu salário mensal: "))
print()
percentual_reajuste = int(input("Digite o percentual de reajuste do salário: "))
print()

# (Processamento) - Calculando novo salário
percentual_decimal = percentual_reajuste/ 100
novo_salario = salario_mensal + (salario_mensal * percentual_decimal)

# (Saída) - Apresentando resultado
print(f"O seu salário com novo percentual de reajuste ficaria: R${novo_salario}")