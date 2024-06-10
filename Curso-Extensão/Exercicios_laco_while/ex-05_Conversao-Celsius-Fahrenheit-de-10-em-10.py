# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: 5) Elaborar um programa que apresente os valores de conversão de graus Celsius em Fahrenheit,
#  de 10 em 10 graus, iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius.
# O programa deve apresentar os valores das duas temperaturas.
# A fórmula de conversão é F = 9C+160/5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

# Apresentação do Programa
print("Conversão de graus Celsius em Fahrenheit de 10 em 10 graus, de 10°C a 100°C")

# Processamento
celsius = 10

while celsius <= 100:
    fahrenheit = (9 * celsius + 160) / 5
    print(f"{celsius}°C = {fahrenheit:.1f}°F")
    celsius += 10
