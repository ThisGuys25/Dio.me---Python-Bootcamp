contatos = {
    "osvaldo@gmail.com": {"nome": "Osvaldo", "numero": 11922345},
    "marcelo@gmail.com": {"nome": "Marcelo", "numero": 119794455},
    "junior@gmail.com": {"nome": "Junior", "numero": 11423156},
    "paulo@gmail.com": {"nome": "Paulo", "numero": 11507231}
}

pessoa = {"b":"bola"}
pessoa["a"] = 1234


#metodo copy
"""
copia = contatos.copy()
copia["osvaldo@gmail.com"] = {"nome":"Oliver"}
print(copia,"\n",contatos)
"""

#fromkeys cria chaves com o valor NONE atribuido, você pode atribuir seu próprio valor também
"""
dicionario = dict.fromkeys(["nome", "telefone"])
print(dicionario)
dicionario_2 = dict.fromkeys(["nome", "telefone"], "vazio")
print(dicionario_2)
"""
#get é usado para acessar valores de um dicionário, caso a chave não exista, é retornado "none" ou um valor personalizado como resposta
"""
dicionario = {"nome":"paulo"}
print(dicionario.get("nome"))
print(dicionario.get("numero"))
print(dicionario.get("numero","nada"))
"""

#setdefault cria uma chave se for necessário e da valor a ela, mas só em casos de necessidade, se chave já foi criada ele respeita o valor dela e não altera