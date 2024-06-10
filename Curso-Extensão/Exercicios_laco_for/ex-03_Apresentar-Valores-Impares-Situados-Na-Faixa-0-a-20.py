# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: 3) Apresentar todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20.
# Para verificar se o número é ímpar, efetuar dentro da malha a verificação lógica desta condição
#  com a instrução se, perguntando se o número é ímpar; sendo, mostre-o; não sendo, passe para o próximo passo.

# Apresentação
print("Apresentar todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20")

for num in range(21):
    # Verifica se o número é ímpar
    if num % 2 != 0:
        # Se for ímpar, mostra-o
        print(num)
