"""
T = int(input())

for i in range(T):
    N, K = list(input().split())
    refrigerantes = int(N) 
    garrafas_vazias = int(K)
    contador = 0
    if refrigerantes < garrafas_vazias:
        print(refrigerantes)
    
    elif refrigerantes > garrafas_vazias:
        while(refrigerantes > garrafas_vazias):
            refrigerantes -= garrafas_vazias
            contador += 1
        valor_maximo = contador +(refrigerantes)
        print(valor_maximo)
"""


a = input() 
b = input() 
c = input() 

if a == 'vertebrado': 
    vertebrado = {"ave":{"carnivoro": "aguia", "ornivoro":"pomba"}, 
              "mamifero":{"ornivoro":"homem", "herbivoro":"vaca"}}
    print(vertebrado[b][c])

elif a == 'invertebrado':
  invertebrado = {"inseto":{"hematofago": "pulga", "herbivoro":"largata"}, 
              "anelideo":{"hematofago":"sanguessuga", "onivoro":"minhoca"}}
  print(invertebrado[b][c])