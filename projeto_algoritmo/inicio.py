def logar():
    login = open("usuarios.txt", "r")
    while True:
        cpf1 = input("Digite o seu CPF: ")
        senha = input("Digite a senha: ")
        erro = 0
        for linha in login.readlines():
            erro += 1
            cpf = ""
            senha1 = ""
            for i in range(11):
                cpf += linha[7+i]
            for i in range(6):
                senha1 += linha[26+i]
            if cpf1 == cpf and senha == senha1:
                print("Login realizado com sucesso")
                return cpf
        if erro != 0:
            print("login falhou, login ou senha errada")
# ========================================================== #
def saldo(cpf):
    contas = open("contas.txt", "r")
    nome = ""
    real = ""
    btc = ""
    eth = ""
    xrp = ""
    erro = 1
    for linha in contas.readlines():
        tmp = ""
        if erro == 1:
            for i in range(11):
                tmp += linha[5 + i]
            if tmp == cpf:
                i = 23
                while True:
                    if linha[i] != " ":
                        if linha[i] == "_":
                            nome += " "
                        else:
                            nome += linha[i]
                    else:
                        break
                    i += 1
                erro = 0
            else:
                erro += 1
        elif erro == 0:
            if linha[0] == 'R':
                i = 6
                while i != len(linha)-1:
                    real += linha[i]
                    i += 1

            elif linha[0] == 'B':
                i = 5
                while i != len(linha)-1:
                    btc += linha[i]
                    i += 1
            elif linha[0] == 'E':
                i = 5
                while i != len(linha)-1:
                    eth += linha[i]
                    i += 1
            elif linha[0] == 'X':
                i = 5
                while i != len(linha)-1:
                    xrp += linha[i]
                    i += 1
                erro = 6
        elif erro == 6:
            erro = 1
        else:
            erro += 1
            continue
    print(f"Nome: {nome}")

    print("CPF: ",end="")
    for i in range(11):
        print(cpf[i],end="")
        if i == 2 or i == 5:
            print(".",end="")
        if i == 8:
            print("-",end="")
    print()
    print(f"Reais: {real}")
    print(f"Bitcoin: {btc}")
    print(f"Ethereum: {eth}")
    print(f"Ripple: {xrp}")
# ========================================================== #
def depositar(cpf):
    contas = open("contas.txt", "r")
    lista = []
    real = ""
    real1 = float((input("Digite o valor em Real a ser depositado: ")))
    erro = 1
    for linha in contas.readlines():
        tmp = ""
        if erro == 1:
            lista.append(linha)
            for i in range(11):
                tmp += linha[5 + i]
            if tmp == cpf:
                erro = 0
            else:
                erro += 1
        elif erro == 0:
            if linha[0] == 'R':
                i = 6
                while i != len(linha)-1:
                    real += linha[i]
                    i += 1
                real = float(real)
                real += real1
                real = str(real)
                lista.append(f"REAL: {real}\n")
            elif linha[0] == 'X':
                lista.append(linha)
                erro = 6
            else:
                lista.append(linha)
        elif erro == 6:
            lista.append(linha)
            erro = 1
        else:
            lista.append(linha)
            erro += 1
            continue
    
    contas = open("contas.txt", "w")

    for i in range(len(lista)):
        contas.write(lista[i])
    
    contas.close()

    print("CPF: ",end="")
    for i in range(11):
        print(cpf[i],end="")
        if i == 2 or i == 5:
            print(".",end="")
        if i == 8:
            print("-",end="")
    print()
    print(f"Reais: {real}")
# ========================================================== #
def sacar(cpf):
    contas = open("contas.txt", "r")
    lista = []
    real = ""
    erro = 1
    for linha in contas.readlines():
        tmp = ""
        if erro == 1:
            lista.append(linha)
            for i in range(11):
                tmp += linha[5 + i]
            if tmp == cpf:
                erro = 0
            else:
                erro += 1
        elif erro == 0:
            if linha[0] == 'R':
                i = 6
                while i != len(linha)-1:
                    real += linha[i]
                    i += 1
                real = float(real)
                while True:
                    real1 = float((input("Digite o valor em Real a ser sacado: ")))
                    if real < real1:
                        print("impossivel realizar esta ação, digite um novo valor:")
                    else:
                        break
                real -= real1
                real = str(real)
                lista.append(f"REAL: {real}\n")
            elif linha[0] == 'X':
                lista.append(linha)
                erro = 6
            else:
                lista.append(linha)
        elif erro == 6:
            lista.append(linha)
            erro = 1
        else:
            lista.append(linha)
            erro += 1
            continue
    
    contas = open("contas.txt", "w")

    for i in range(len(lista)):
        contas.write(lista[i])
    
    contas.close()

    print("CPF: ",end="")
    for i in range(11):
        print(cpf[i],end="")
        if i == 2 or i == 5:
            print(".",end="")
        if i == 8:
            print("-",end="")
    print()
    print(f"Reais: {real}")
# ========================================================== #
def comprar(cpf):
    contas = open("contas.txt", "r")
    moedas = open("moedas.txt", "r")
    
# ========================================================== #
def menu(cpf):
    print("------------------------")
    print("Menu")
    print("------------------------")
    print("1 - Consultar Saldo")
    print("2 - Consultar Extrato")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Comprar Criptomoedas")
    print("6 - Vender Criptomoedas")
    print("7 - Atualizar Cotação")
    print("8 - Sair")
    print("------------------------")
    while True:
        id = int(input("Digite o numero da ação desejada: "))
        if id == 1:
            saldo(cpf)
        if id == 2:
            print("check")
            extrato(cpf)
        if id == 3:
            depositar(cpf)
        if id == 4:
            print("check")
            sacar(cpf)
        if id == 5:
            print("check")
            comprar(cpf)
        if id == 6:
            print("check")
            vender(cpf)
        if id == 7:
            print("check")
            atualizar(cpf)
        if id == 8:
            break

# ========================================================== #

while True:
    cpf = logar()
    menu(cpf)