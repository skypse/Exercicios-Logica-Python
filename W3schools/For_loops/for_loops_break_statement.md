A declaração 'break' com a instrução break podemos parar o loop antes que ele tenha percorrido todos os itens

Exemplo: Sair do ciclo quando x for “banana”:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

output ficaria:
apple
banana