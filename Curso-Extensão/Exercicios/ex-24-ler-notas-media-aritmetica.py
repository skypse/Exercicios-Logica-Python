# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

# (Saída) - Apresentação
print("Programa que calcula a média aritmética das notas dos alunos.")
print()

# (Entrada) - Pedindo dados e Armazenando
nota1 = float(input("Qual a primeira nota do aluno: "))
nota2 = float(input("Qual a segunda nota do aluno: "))
print()

# (Processamento) - Calculando média aritmética
media = (nota1+nota2) / 2

# (Saída) - Exibindo resultados
print(f"A média total do aluno foi {media}")