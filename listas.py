numero = list( "123456")
inverso = ""
for indice, valor in enumerate(numero):
    inverso += numero[(indice +1)*(-1)]
print(inverso)