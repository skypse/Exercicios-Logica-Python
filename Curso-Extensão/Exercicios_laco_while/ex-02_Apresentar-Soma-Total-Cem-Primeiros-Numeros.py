# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: 2) Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100).

# Apresentação Programa
print("Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100)")

# Processamento
contadora = 1
soma = 0

while contadora <= 100:
    soma += contadora
    contadora += 1

print(f"A soma total foi de: {soma}")
