# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5. Fórmula para o cálculo da média final é: mediafinal =(n1 * 2 + n2 * 3 + n3 * 5)/10


# (Saída) - Apresentação
print("Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius.")
print()

# (Entrada) - Pedindo os dados e armazenando
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

# (Processamento) - Efetuando o calculo da média
mediafinal = (nota1 * 2 + nota2 * 3 + nota3 * 5)/10

# (Saída) - Apresentando resultado
print(f"A média final foi {mediafinal}")

