A instrução 'continue'. Com a instrução continue, podemos parar a iteração atual do ciclo e continuar com a seguinte:

Exemplo: Não imprimir banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)