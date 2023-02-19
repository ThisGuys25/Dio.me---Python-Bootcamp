numeros = [1, 30, 22, 40, 60, 13, 99, 88]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)




#aplicando o metodo de compreension
impares = [numero for numero in numeros if numero % 2 != 0]
print(impares)