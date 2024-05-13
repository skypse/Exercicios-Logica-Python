# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

# (Saída) - Apresentação
print("Programa que calcula o custo total das maças")
print()

# (Entrada) - Pedindo dados e Armazenando
macas_preco = 1.30

print("Se comprar mais de 1 dúzia cada maça sai por R$1,00")
print()
macas_quantidade = int(input("Quantas maças você comprou? "))

# (Processamento) - Efetuando calculo e verificação
if macas_quantidade >= 12:
  resultado = macas_quantidade * 1
  print(f"Você comprou {macas_quantidade} maças, e ganhou um desconto, ficando no total R${round(resultado,2)}")
else:
  resultado = macas_quantidade * macas_preco
  print(f"Você comprou {macas_quantidade} maças, e o total ficou R${round(resultado,2)}")