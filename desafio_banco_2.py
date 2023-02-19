contas = {"conta":[{"1":{"id":"0002","agencia":"bradesco","extrato":{"saldo":500, "saques":3}}},
                        {"1":{"id":"0001","agencia":"bradesco","extrato":{"saldo":500, "saques":3}}},
                        {"2":{"id":"0001","agencia":"bradesco","extrato":{"saldo":900, "saques":3}}}]}

def sacar(*,valor, cpf, conta_corrente):
    contador = 0
    for i in contas["conta"]:
        try:
            if conta_corrente == contas["conta"][contador][cpf]["id"]: 
                contas["conta"][contador][cpf]["extrato"]["saldo"] -= valor
                print("\nEfetuando o saque...")
                sleep(2)
                print("Saque efetuado com sucesso!")
                print(f"Saldo atual: R${contas['conta'][contador][cpf]['extrato']['saldo']}")
                sleep(3)
                break
        except KeyError:
            contador += 1
            
        else:
            contador += 1

def consultar(cpf, conta_corrente):
    contador = 0
    for i in contas["conta"]:
        try:
            if conta_corrente == contas["conta"][contador][cpf]["id"]: 
                print("Efetuando consulta...")
                sleep(2)
                print(f"Saldo atual: R${contas['conta'][contador][cpf]['extrato']}")
                sleep(3)
                break
        except KeyError:
            contador += 1
            
        else:
            contador += 1


def novo_cliente(nome, data, cpf, endereco):
    clientes.append([nome, data, cpf, endereco])
    print(clientes)
def conta_corrente(cpf, agencia, saldo):
    global  contas
    contas["conta"].append({f"{cpf}":{"id":"","agencia":agencia,"extrato":{"saldo":saldo, "saques":3}}})
    print(contas["conta"])

def depositar(valor, cpf, conta_corrente,/):
    contador = 0
    for i in contas["conta"]:
        try:
            if conta_corrente == contas["conta"][contador][cpf]["id"]: 
                contas["conta"][contador][cpf]["extrato"]["saldo"] += valor
                print("\nEfetuando o depósito...")
                sleep(2)
                print("Depósito efetuado com sucesso!")
                print(f"Saldo atual: R${contas['conta'][contador][cpf]['extrato']['saldo']}")
                sleep(3)
                break
        except KeyError:
            contador += 1
            
        else:
            contador += 1


def banco():
    while True:
        acao = int(input(
"""
BEM VINDO(A) AO BANCO MAPHRA!    
Aqui vão algumas operações bancárias que você pode realizar:
        
    [1] Depósito.
    [2] Saque.
    [3] Consultar o extrato
    [4] Criar conta corrente
    [5] Criar sua conta(novo cliente).
    [6] Sair.

Qual operação bancária você deseja realizar: """))
        if acao == 6:
            break
        elif acao == 1:
            depositar(float(input("Digite o valor do depósito: ")), input("Digite seu cpf: "), input("digite a conta corrente: "))
        
        elif acao == 2:
            print("\nlimite de 3 saques e valor máximo de R$500,00")
            sacar(valor=float(input("Digite o valor do saque: ")), cpf=input("Digite seu cpf: "), conta_corrente=input("Digite a conta corrente: "))
        
        elif acao == 3:
            consultar(input("Digite seu cpf: "), input("Digite a conta corrente que deseja consultar: "))
        
        elif acao == 4:
            cpf = input("Digite seu cpf: ")
            contador = 0
            for i in clientes:
                if cpf in i:
                    conta_corrente(cpf, input("Digite o nome da agência: "), float(input("Digite o saldo: ")))
                    for i in contas["conta"]:
                        if cpf in i:
                            contador += 1
                    i[cpf]["id"] = f"000{contador}"
       
        elif acao ==  5:
            print("Digite seu endereço:\n")
            endereco = {"logradouro":input("logradouro: "), "nmr":input("número: "), "bairro":input("bairro: "), "cidade/sigla":input("cidade/sigla: "), "estado":input("estado: ")}
            novo_cliente(input("digite seu nome completo: "), input("digite a data de nascimento: "), input("digite seu cpf: "), endereco)


if __name__ == "__main__":
    from time import sleep
    clientes = []
    banco()
