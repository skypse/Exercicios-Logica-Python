# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: 5) Elaborar um programa que apresente os valores de conversão de graus
#  Celsius em Fahrenheit, de 10 em 10 graus, iniciando a contagem em 10 graus Celsius
#  e finalizando em 100 graus Celsius. O programa deve apresentar os valores das duas temperaturas.
#  A fórmula de conversão F = (9C +160)/5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

# Apresentação
print("Apresentar os valores de conversão de graus Celsius em Fahrenheit, de 10 em 10 graus")

# Processamento
inicio_celsius = 10
fim_celsius = 100

# Apresentação dos valores de conversão
print("Temperatura em Celsius | Temperatura em Fahrenheit")
print("-" * 50)

# Iteração de 10 em 10 graus Celsius
for celsius in range(inicio_celsius, fim_celsius + 1, 10):
    # Calcula a temperatura em Fahrenheit
    fahrenheit = (9 * celsius + 160) / 5
    # Apresenta os valores de temperatura em Celsius e Fahrenheit
    print(f"{celsius:^4} | {fahrenheit:^4}")
