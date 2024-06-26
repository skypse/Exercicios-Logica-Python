# Argumentos
# As informações podem ser passadas para as funções como argumentos.

# Os argumentos são especificados após o nome da função, dentro de parênteses. Pode adicionar tantos argumentos quantos quiser, basta separá-los com uma vírgula.

# O exemplo seguinte tem uma função com um argumento (fname). Quando a função é chamada, passamos um primeiro nome, que é utilizado dentro da função para imprimir o nome completo:

def my_function(fname, lname):
    print(fname + lname)


my_function("Gabriel", " do Amaral")
my_function("João", " Eduardo")
my_function("Guilherme", " Freitas")
