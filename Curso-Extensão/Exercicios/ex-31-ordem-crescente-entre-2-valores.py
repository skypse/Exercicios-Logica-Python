# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

# (Saída) - Apresentação
print("Ler dois valores e escrevê-los em ordem crescente.")
print()

# (Entrada) - Pedindo dados e armazenando
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

# (Processamento) - Ordenando os valores
if valor1 < valor2:
    menor_valor = valor1
    maior_valor = valor2
else:
    menor_valor = valor2
    maior_valor = valor1

# (Saída) - Exibindo os valores em ordem crescente
print("Valores em ordem crescente:", menor_valor, ",", maior_valor)
