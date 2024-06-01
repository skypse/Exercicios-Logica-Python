Else em um loop for:
A palavra-chave else num ciclo for especifica um bloco de código a ser executado quando o ciclo terminar.
Exemplo: Imprimir todos os números de 0 a 5 e imprimir uma mensagem quando o ciclo terminar:
for x in range(6):
    print(x)
else:
    print("Finally finished!")

O output ficaria assim:
0
1
2
3
4
5
Finally finished!


# Note: The else block will NOT be executed if the loop is stopped by a break statement.
Exemplo: Interrompa o loop quando x for 3 e veja o que acontece com o bloco else:

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")
Se o loop for interrompido, o bloco else não é executado.