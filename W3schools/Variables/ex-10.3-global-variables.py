# também se você usar 'global', se você quiser trocar o valor de uma variável global, dentro da function
# para mudar o valor de uma variável 'global', dentro da function, fazendo referência usando a palavra chave 'global'

# variável global
x = "awesome"

def myfunc():
  # tornando variável 'x' global
  global x
  # trocando o valor dela
  x = "fantastic"

myfunc()

# puxando a variável global com o valor mudado!
print("Python is " + x)