# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: 4) Apresentar todos os números divisíveis por 4 que sejam menores que 200.
#  Para verificar se o número é divisível por 4, efetuar dentro da malha a verificação lógica desta condição com a instrução se,
#  perguntando se o número é divisível; sendo, mostre-o; não sendo, passe para o próximo passo.
#  A variável que controlará o contador deve ser iniciada com o valor 1.

# Apresentação
print("Apresentar todos os números divisíveis por 4 que sejam menores que 200")

# Processamento
contador = 1

while contador < 201:
    # Verifica se o número é divisível por 4
    if contador % 4 == 0:
        # Se for divisível por 4, mostra-o
        print(contador)
    # Incrementa o contador
    contador += 1
