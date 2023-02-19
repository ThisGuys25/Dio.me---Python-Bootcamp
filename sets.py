#retirando números repetidos de uma lista com classe set
lista_numeros = [1, 1, 2, 2, 3, 3]
lista_sem_repetir = set(lista_numeros)



#métodos com a classe set

#union, une dois conjuntos
"""
conjunto_a = {1, 2}
conjunto_b = {3, 4}
print(conjunto_a.union(conjunto_b))
print(conjunto_a)
"""
#Informação interessante, o conjunto_a não teve seu valor inicial modificado, creio que para trabalhar com os valores desse método, eu precise colocar em uma variável


#intersection, compara valores IDENTICOS em dois conjuntos 
"""
conjunto_a = {1, 2, 3, 4}
conjunto_b = {5, 2, 9, 4}
print(conjunto_b.intersection(conjunto_a))
"""

#difference, mostra os valores diferentes dentro do conjunto em comparação ao outro conjunto
"""
conjunto_a = {1, 2, 3, 4}
conjunto_b = {5, 2, 9, 4}
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
"""

#symmetric_difference, funciona como o método difference, porém, você tem as diferenças agregadas a uma mesma variável, tanto as em comparação de A com B, quanto de B com A
"""
conjunto_a = {1, 2, 3, 4}
conjunto_b = {5, 2, 9, 4}
print(conjunto_a.symmetric_difference(conjunto_b))
"""
#issubset, esse método verifica se todos os valores de um conjunto se encontram em outro conjunto comparado e retorna True ou False, dependendo da comparação
"""
conjunto_a = {1, 2, 3, 4}
conjunto_b = {5, 2, 9, 4, 3, 1}
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))
"""


#issuperset, funciona como o método de cima, porém invertido, o valor que é comparado está dentro dos parentesês
"""
conjunto_a = {1, 2, 3, 4}
conjunto_b = {5, 2, 9, 4, 3, 1}
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))
"""
#nesse caso, os valores do conjunto_b estão no conjunto_a, no caso do issubset seria os valores do cojunto_a estão no conjunto_b

#isdisjoint, método usado para dizer por exemplo, se os conjuntos NÃO tem valores iguais, em caso de não ter valores iguais se retorna True, caso contrário, False
"""
conjunto_a = {60, 33, 21, 43}
conjunto_b = {5, 2, 9, 4, 3, 1}
conjunto_c = {5, 2}
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_c.isdisjoint(conjunto_b))
"""

#add, adiciona um valor ao conjunto apenas se o valor não se encontrar no conjunto
"""
numeros = {1, 2}
numeros.add(3)
numeros.add(4)
numeros.add(1)
print(numeros)
"""
#como visto, o número 1 não é adicionado ao conjunto pois já se encontra no mesmo

#discard, usado para discartar um valor de um conjunto, porém, se você selecionar um valor que seu conjunto não tenha, nenhum erro é descrito no terminal
"""
numeros = {10, 20, 30, 40, 50, 51}
numeros.discard(10)
numeros.discard(80)
print(numeros)
"""
