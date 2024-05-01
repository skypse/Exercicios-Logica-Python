# se você criar uma variavel com o mesmo nome, só que dentro da função, essa variável vai se tornar local
# e só poderá ser usada dentro da função. E a variável global ficará com o mesmo nome como estava, com seu valor original

#global
x = "awesome"

def myfunc():
  # local
  x = "fantastic"

  #puxando variável local
  print("Python is " + x)

myfunc()

# puxando variável global
print("Python is " + x)