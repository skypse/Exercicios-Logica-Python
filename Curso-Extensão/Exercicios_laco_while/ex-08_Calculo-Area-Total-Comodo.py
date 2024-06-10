# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: 8) Elaborar um programa que possibilite calcular a área total de uma residência (sala, cozinha,
# banheiro, quartos, área de serviço, quintal, garagem, etc.). O programa deve solicitar a entrada do nome, a largura e o comprimento de um determinado cômodo.
# Em seguida, deve apresentar a área do cômodo lido e também uma mensagem solicitando do usuário a confirmação de continuar calculando novos cômodos.
# Caso o usuário responda “NAO”, o programa deve apresentar o valor total acumulado da área residencial. COM WHILE

# Apresentação do Programa
print("Programa para calcular a área total de uma residência")

# Variavel
area_total = 0

# Loop para calcular a área de cada cômodo
while True:
    # Nome do cômodo
    nome_comodo = input("Digite o nome do cômodo: ")

    # Largura e o comprimento do cômodo
    largura = float(input(f"Digite a largura do {nome_comodo} em metros: "))
    comprimento = float(
        input(f"Digite o comprimento do {nome_comodo} em metros: "))

    # Calcula a área do cômodo
    area_comodo = largura * comprimento
    print(f"A área do {nome_comodo} é: {area_comodo:.2f} metros quadrados")

    # Adiciona a área do cômodo à área total
    area_total += area_comodo

    # Deseja continuar?
    continuar = input(
        "Deseja calcular a área de outro cômodo? (Digite 'NAO' para encerrar ou qualquer outra tecla para continuar): ")

    # Verifica se o usuário deseja encerrar
    if continuar.strip().upper() == 'NAO':
        break

# Apresentação do resultado final
print(f"\nA área total da residência é: {area_total:.2f} metros quadrados")
