# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: 1) Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer.

# Apresentação Programa
print("Apresentar os resultados de uma tabuada, 1 à 10. De um número qualquer!")

# Pedindo o Número
valor = int(input("Digite um número inteiro positivo: "))

# Processamento
contadora = 1

while contadora < 11:
    resultado = valor * contadora
    print(f"{valor} x {contadora} = {resultado}")
    contadora += 1
