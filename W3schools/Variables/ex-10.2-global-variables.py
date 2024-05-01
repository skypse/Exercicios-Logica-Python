# normalmente quando você cria uma variável dentro de uma função, essa variável se torna local e só pode ser usada
# localmente, sendo somente usada dentro da função

# para criar uma variável global dentro de uma função você pode usar 'global'

def myfunc():
  # criando variável global
  global x
  x = "fantastic"
myfunc()

# puxando variável global dentro da funciton
print("Python is " + x)