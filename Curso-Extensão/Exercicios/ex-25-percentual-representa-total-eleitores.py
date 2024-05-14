# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

# (Saída) - Apresentação
print("Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.")
print()

# (Entrada) - Pedindo dados e armazenando
total_eleitores = int(input("Digite o total de eleitores: "))
votos_brancos = int(input("Digite a quantidade de votos brancos: "))
votos_nulos = int(input("Digite a quantidade de votos nulos: "))
votos_validos = int(input("Digite a quantidade de votos validos: "))

# (Processamento) - Calculando a porcentagem dos votos
percentual_votos_brancos = (votos_brancos / 100) * 100
percentual_votos_nulos = (votos_nulos / 100) * 100
percentual_votos_validos = (votos_validos / 100) * 100

# (Saída) - Exibindo resultados
print(f"Total de votos brancos em relação ao total de eleitores foi de: {percentual_votos_brancos}%")
print(f"Total de votos nulos em relação ao total de eleitores foi de: {percentual_votos_nulos}%")
print(f"Total de votos validos em relação ao total de eleitores foi de: {percentual_votos_validos}%")