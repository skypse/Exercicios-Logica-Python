# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100)

# (Saída) - Apresentação
print("Programa que apresenta o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100)")
print()

contadora =1
acumuladora= 0

while contadora < 101:
    acumuladora = acumuladora + contadora
    contadora += 1
    
print(f"A soma total corresponde a: {acumuladora}")