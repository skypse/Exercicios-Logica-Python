# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Apresentar todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20.
# Para verificar se o número é ímpar, efetuar dentro da malha a verificação lógica desta condição com a instrução
# se, perguntando se o número é ímpar; sendo, mostre-o; não sendo, passe para o próximo passo.

# Apresentação Programa
print("Apresentar todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20")

# Processamento
numero = 1

while numero < 20:
    if (numero % 2 != 0):
        print(numero)
    numero += 1
