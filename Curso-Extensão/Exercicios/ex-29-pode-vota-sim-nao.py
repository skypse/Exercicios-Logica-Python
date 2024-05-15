# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

# (Saída) - Apresentação
print("Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu)")
print()

# (Entrada) - Pedindo dados e armazenando
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))

# (Processamento) - Calculando a idade
idade = ano_atual - ano_nascimento

# (Saída) - Verificando se a pessoa pode votar
if idade >= 16:
    print("Você pode votar este ano!")
else:
    print("Você ainda não pode votar este ano.")
