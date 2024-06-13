# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um programa que leia a nota de um aluno e converta-a para conceito:
#            A (nota >= 9)
#            B (7 <= nota < 9)
#            C (5 <= nota < 7)
#            D (3 <= nota < 5)
#            F (nota < 3)

# leitura da nota do aluno
nota = float(input("Digite a nota do aluno: "))

# conversão da nota para conceito
if nota >= 9:
    conceito = "A"
elif nota >= 7:
    conceito = "B"
elif nota >= 5:
    conceito = "C"
elif nota >= 3:
    conceito = "D"
else:
    conceito = "F"

# exibição do conceito correspondente
print(f"Conceito: {conceito}")
