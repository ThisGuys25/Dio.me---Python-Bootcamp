from time import sleep 
def menu():
    try:
        operacao = int(input(
        """
BEM VINDO(A) AO BANCO MAPHRA!    
Aqui vão algumas opções operações bancárias que você pode realizar:
        
    [1] Depósito.
    [2] Saque.
    [3] Consultar o extrato
    [4] Sair.

Qual operação bancária você deseja realizar: """))
        
    except ValueError:
        print("Selecione um valor correto!")
        sleep(4)
    
    else:
        if operacao > 4 or operacao == 0:
            print("Selecione um valor correto!")
            sleep(4)
        else:
            return operacao
        

if __name__ == "__main__":
    extrato = {"depositos":[],"saques":[], "saldo":0}
    while True:
        operacao= menu()
        if operacao == 4:
            print("Volte sempre!")
            sleep(3)
            break

        elif operacao == 1:
            deposito = float(input("Digite o valor do depósito: "))
            print("depositando...")
            sleep(2)
            extrato["saldo"] += deposito
            extrato["depositos"].append(f"R${deposito:.2f}")
            print("depósito efetuado com sucesso!")
            sleep(3)
        
        elif operacao == 2:
            saque = float(input("Digite o valor do saque: "))
            
            if saque > 500 or saque  <= 0:
                print("Você só pode sacar valores de até no máximo R$500,00 ou maiores que 0.")
                sleep(2)
            
            elif saque <= extrato["saldo"] and len(extrato["saques"]) < 3:
                extrato["saldo"] -= saque
                extrato["saques"].append(f"R$ {saque:.2f}")
                print(f"O valor de R${saque} foi debitado do seu saldo...")
            
            
            else:
                print("Saldo insuficiente ou número de saques excedidos...")    
                sleep(3)

        elif operacao == 3:
            for i in extrato:
                print(f"{i}:",f"R${extrato[i]}")
            sleep(4)
                 
        
