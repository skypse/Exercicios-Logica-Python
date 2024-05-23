# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma mensagem informando esta condição. Apresentar junto das mensagens o valor da média do aluno para qualquer condição.

# (Saída) - Apresentação
print("Programa que verifica se o aluno foi aprovado sim ou não")
print()

# (Entrada) - Pedindo valores e armazenando
nota1 = int(input("Digite a primeira nota do Aluno: "))
nota2 = int(input("Digite a segunda nota do Aluno: "))
nota3 = int(input("Digite a terceira nota do Aluno: "))
nota4 = int(input("Digite a quarta nota do Aluno: "))

# (Processamento) - Efetuando a verificação e calculando
media = (nota1+nota2+nota3+nota4) / 4

if media < 5:
  print(f"O aluno não foi aprovado!\nPois a média final dele foi: {media}")
else:
  print(f"O aluno foi aprovado!\nCom a média final de: {media}")