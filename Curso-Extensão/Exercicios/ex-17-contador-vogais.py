# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Contagem de vogais em uma frase

# Programa para contar quantas vogais (a, e, i, o, u) uma frase possui

# (Saída) - Apresentação
print("Contagem de vogais em uma frase")


# (Entrada) - Pedindo uma frase e armazenando
frase = input("Digite uma frase: ")

# (Processamento) - Inicializando o contador de vogais
contador_vogais = 0

# (Processamento) - Iterando sobre cada caractere da frase para contar as vogais
for caractere in frase:
    # Verificando se o caractere é uma vogal
    if caractere.lower() in 'aeiou':
        contador_vogais += 1

# (Saída) - Exibindo o número de vogais encontradas na frase
print("A frase possui", contador_vogais, "vogais.")
