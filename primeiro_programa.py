n = int(input())

while (n > 0):
    primeiro_numero, segundo_numero = list(input().split())
    print(primeiro_numero[-len(segundo_numero):])
    if primeiro_numero[-len(segundo_numero):] == segundo_numero:
        print("encaixa")
    else:
        print("nao encaixa")
    n -= 1
    