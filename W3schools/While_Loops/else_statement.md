Com a instrução 'else', podemos executar um bloco de código uma vez quando a condição deixa de ser verdadeira.
Exemplo: Imprimir uma mensagem quando a condição for falsa:
i = 1

    while i < 6:
        print(i)
        i += 1
else:
  print("i is no longer less than 6")

O output ficaria assim:
1
2
3
4
5
i is no longer less than 6