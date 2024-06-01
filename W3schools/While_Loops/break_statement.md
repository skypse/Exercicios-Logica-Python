Utilizando o break statement

Com a instrução break, podemos parar o ciclo mesmo que a condição while seja verdadeira, Exemplo:
- Sair do loop quando o 'i' chegar em 3:

i = 1
while i < 6:
    print(i)
    if (i == 3):
        break
    i += 1
