adjetivo = ["Vermelho", "Grande", "Saboroso"]
fruta = ["Damasco", "Maça", "Ameixa"]

for x in adjetivo:
    for y in fruta: # esse loop será executado até o final para que o loop de fora seja executado novamente e entre em outro loop
        print(x, y)
