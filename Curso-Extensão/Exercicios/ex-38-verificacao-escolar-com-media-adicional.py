# Curso Básico de Python
# Nome: Gabriel do Amaral Alves
# Versão 1.0
# Exercício de Lógica de Programação utilizando Python
# Enunciado: Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 7. Se o valor da média for menor que 7, solicitar a nota de exame, somar com o valor da média e obter nova média. Se a nova média for maior ou igual a 5, apresentar uma mensagem dizendo que o aluno foi aprovado em exame. Se o aluno não foi aprovado, indicar uma mensagem informando esta condição. Apresentar com as mensagens o valor da média do aluno, para qualquer condição.

# (Saída) - Apresentação
print("Programa que verifica a aprovação com exame final")
print()

# (Entrada) - Pedindo valores e armazenando
nota1 = int(input("Digite a primeira nota do Aluno: "))
nota2 = int(input("Digite a segunda nota do Aluno: "))
nota3 = int(input("Digite a terceira nota do Aluno: "))
nota4 = int(input("Digite a quarta nota do Aluno: "))

# (Processamento) + (Saída) - Efetuando a verificação e calculando
media = (nota1+nota2+nota3+nota4) / 4

if media >= 7:
  print(f"O aluno foi aprovado!\nCom a média final de: {media}")
else:
  nota5 = int(input("Digite uma nota de algum exame adicional: "))
  nova_media = (media + nota5) / 2

  if nova_media >= 5:
    print(f"O aluno foi aprovado em exame!\nCom a nova média final de: {nova_media}")
  else:
    print(f"O aluno não foi aprovado.\nCom a nova média final de: {nova_media}")