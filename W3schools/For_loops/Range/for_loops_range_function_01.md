A função range()
Para percorrer um conjunto de código um número especificado de vezes, podemos utilizar a função range().
A função range() devolve uma sequência de números, começando em 0 por predefinição, aumentando em 1 (por predefinição) e terminando num número especificado.

Exemplo: Utilizar a função range():
for x in range(6):
  print(x)

O output ficaria assim:
0
1
2
3
4
5

A função range() tem como predefinição 0 como valor inicial, mas é possível especificar o valor inicial adicionando um parâmetro: range(2, 6), que significa valores de 2 a 6 (mas não incluindo 6):
Exemplo de utilização: Utilizando o parâmetro:
for x in range(2, 6):
  print(x)

O output ficaria assim:
2
3
4
5