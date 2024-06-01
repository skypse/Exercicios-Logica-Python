Laços aninhados
Um loop encadeado é um loop dentro de um loop.
O “loop interno” será executado uma vez por cada interação do “loop externo”. Exemplo: Imprimir cada adjetivo para cada fruta:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

O output será:
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry