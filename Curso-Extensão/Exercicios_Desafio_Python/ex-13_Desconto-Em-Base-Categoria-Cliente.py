# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Escreva um programa que leia o valor de uma compra e a categoria do cliente:
#            1 para comum, 2 para associado e 3 para VIP. Aplique os seguintes descontos:
#            Comum: Sem desconto
#            Associado: 10% de desconto
#            VIP: 20% de desconto
#            Informe o valor final da compra.

# leitura do valor da compra e da categoria do cliente
valor_compra = float(input("Digite o valor da compra: "))
categoria_cliente = int(input("Digite a categoria do cliente (1 para comum, 2 para associado, 3 para VIP): "))

# aplicação do desconto conforme a categoria do cliente
if categoria_cliente == 1:
    valor_final = valor_compra  # sem desconto para cliente comum
    categoria = "comum"
elif categoria_cliente == 2:
    valor_final = valor_compra * 0.9  # 10% de desconto para cliente associado
    categoria = "associado"
elif categoria_cliente == 3:
    valor_final = valor_compra * 0.8  # 20% de desconto para cliente VIP
    categoria = "VIP"
else:
    print("Categoria inválida.")
    valor_final = None
    categoria = "inválida"

# exibição do valor final da compra, se a categoria for válida
if valor_final is not None:
    print(f"Valor final da compra para cliente {categoria}: R$ {valor_final:.2f}")
