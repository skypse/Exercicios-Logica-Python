# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um programa que leia três notas de um aluno e calcule a média.
#            Informe se o aluno está aprovado (média >= 7), em recuperação (5 <= média < 7)
#            ou reprovado (média < 5).

# leitura das três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# cálculo da média
media = (nota1 + nota2 + nota3) / 3

# verificação da situação do aluno
if media >= 7:
    print(f"Com média {media:.2f}, o aluno está APROVADO.")
elif media >= 5:
    print(f"Com média {media:.2f}, o aluno está em RECUPERAÇÃO.")
else:
    print(f"Com média {media:.2f}, o aluno está REPROVADO.")
