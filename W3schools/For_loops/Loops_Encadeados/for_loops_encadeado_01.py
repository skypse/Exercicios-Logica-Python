adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits: # esse loop será executado até o final para que o loop de fora seja executado novamente e entre em outro loop
        print(x, y)
