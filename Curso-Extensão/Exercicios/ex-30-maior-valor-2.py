# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

# Programa que peça ao usuário para digitar três números e retorne o maior deles

# (Saída) - Apresentação
print("Usuário para digita três números e o programa retorna o maior deles!")
print()

# (Entrada) - Pedindo dados e armazenando
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# (Processamento) - retornando o maior número
maior_numero = max(numero1,numero2)

# (Saída) - Exibindo o maior número
print("O maior número é:", maior_numero)