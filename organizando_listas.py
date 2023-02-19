linguagens = ["python", "java", "js", "c", "csharp"]
linguagens.sort(key=lambda x:len(x))


#explicando a função
"""Basicamente o key=lambda, é uma função anônima,
para cada item dentro da nossa lista, vai ser feita uma comparação de tamanho, sendo x cada elemento e len(x) o tamanho desse elemento,
ordenando sua lista do menor len ao maior. Caso você queira ver do maior len ao menor você aplica o modo reverse=True, tornando sua lista do maior len ao menor
exemplo: linguagens.sort(key=lambda x:len(x), reverse=True)"""
print(linguagens)

numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(numeros)