A instrução 'continue' podemos parar a interação atual e continuar com a seguinte, utilizando 'continue' para a interação seguinte se i for 3:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)