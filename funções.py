#funções retornam tuplas por padrão, se você quiser dicionários, precisa adcionar os ** na hora de chamar a função: função(**informação)
#se você tem um dicionário com os mesmos argumentos que uma função, é só você passar o dicionário dessa maneira:

def carro(marca, modelo):
    print(marca, modelo)


dicionario = {"marca":"bmw", "modelo":"i8"}
carro(**dicionario)
#ou carro(**{"marca":"bmw", "modelo":"i8"})

#positiononly / (modelo, placa, pessoa,/)
#keywordonly * (*,modelo="nome do carro", placa="placa do carro", pessoa="diego")
