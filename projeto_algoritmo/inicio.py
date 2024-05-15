from random import randint
def logar():
    while True:
        login = open("usuarios.txt", "r")
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
            login.close()
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
                    if i < len(linha)-1:
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
                lista.append(f"REAL: {real:.2f}\n")
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
                lista.append(f"REAL: {real:.2f}\n")
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
# ========================================================== #
def comprar(cpf):
    moeda = input("Digite a moeda desejada (btc, eth ou xrp): ")
    contas = open("contas.txt", "r")
    moedas = open("moedas.txt", "r")
    lista = []
    real = ""
    real1 = 0
    valor = ""
    ct = ""
    txc = ""
    erro = 1
    for linha in moedas.readlines():
        if (linha[0] == 'X' and moeda == "xrp")or(linha[0] == 'B' and moeda == "btc")or(linha[0] == 'E' and moeda == "eth"):
            comeco = ""
            for i in range(9):
                comeco += linha[i]
            i = 9
            while linha[i] != " ":
                ct += linha[i]
                i += 1
            j =  i + 6
            while linha[j] != "%":
                txc += linha[j]
                j += 1
            txc = float(txc)
            resto = ""
            while i != len(linha)-1:
                resto += linha[i]
                i += 1
            ct = float(ct)
    moedas.close()
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
                    real1 = float((input("Digite o valor em reais da compra: ")))
                    if real < real1:
                        print("impossivel realizar esta ação, digite um novo valor:")
                    else:
                        break
                real -= real1
                lista.append(f"REAL: {real:.2f}\n")
            elif linha[0] == 'B' and moeda == "btc":
                i = 5
                while i != len(linha)-1:
                    valor += linha[i]
                    i += 1
                valor = float(valor)
                valor += real1/ct
                valor -= valor*txc
                lista.append(f"BTC: {valor:.3f}\n")
            elif linha[0] == 'E' and moeda == "eth":
                i = 5
                while i != len(linha)-1:
                    valor += linha[i]
                    i += 1
                valor = float(valor)
                valor += real1/ct
                lista.append(f"ETH: {valor:.3f}\n")
            elif linha[0] == 'X' and moeda == "xrp":
                i = 5
                while i != len(linha)-1:
                    valor += linha[i]
                    i += 1
                valor = float(valor)
                valor += real1/ct
                lista.append(f"XRP: {valor:.3f}\n")
                erro = 6
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
# ========================================================== #
def vender(cpf):
    moeda = input("Digite a moeda desejada (btc, eth ou xrp): ")
    contas = open("contas.txt", "r")
    moedas = open("moedas.txt", "r")
    lista = []
    real = ""
    real1 = 0
    cont = -1
    valor = ""
    valor1 = 0
    ct = ""
    txv = ""
    erro = 1
    for linha in moedas.readlines():
        if (linha[0] == 'X' and moeda == "xrp")or(linha[0] == 'B' and moeda == "btc")or(linha[0] == 'E' and moeda == "eth"):
            comeco = ""
            for i in range(9):
                comeco += linha[i]
            i = 9
            while linha[i] != " ":
                ct += linha[i]
                i += 1
            j =  i + 17
            while linha[j] != "%":
                txv += linha[j]
                j += 1
            txv = float(txv)
            resto = ""
            while i != len(linha)-1:
                resto += linha[i]
                i += 1
            ct = float(ct)
    moedas.close()
    for linha in contas.readlines():
        if real1 == 0:
            cont += 1
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
                real1 = cont
                lista.append(linha)
            elif linha[0] == 'B' and moeda == "btc":
                i = 5
                while i != len(linha)-1:
                    valor += linha[i]
                    i += 1
                valor = float(valor)
                while True:
                    valor1 = float((input(f"Digite o valor em {moeda} da venda: ")))
                    if valor < valor1:
                        print("impossivel realizar esta ação, digite um novo valor:")
                    else:
                        break
                valor -= valor1
                real = real + valor1*ct
                real -= real*txv
                lista[real1] = f"REAL: {real:.2f}\n"
                lista.append(f"BTC: {valor:.3f}\n")
            elif linha[0] == 'E' and moeda == "eth":
                i = 5
                while i != len(linha)-1:
                    valor += linha[i]
                    i += 1
                valor = float(valor)
                while True:
                    valor1 = float((input(f"Digite o valor em {moeda} da venda: ")))
                    if valor < valor1:
                        print("impossivel realizar esta ação, digite um novo valor:")
                    else:
                        break
                valor -= valor1
                real = real + valor1*ct
                real -= real*txv
                lista[real1] = f"REAL: {real:.2f}\n"
                lista.append(f"ETH: {valor:.3f}\n")
            elif linha[0] == 'X' and moeda == "xrp":
                i = 5
                while i != len(linha)-1:
                    valor += linha[i]
                    i += 1
                valor = float(valor)
                while True:
                    valor1 = float((input(f"Digite o valor em {moeda} da venda: ")))
                    if valor < valor1:
                        print("impossivel realizar esta ação, digite um novo valor:")
                    else:
                        break
                valor -= valor1
                real = real + valor1*ct
                real -= real*txv
                lista[real1] = f"REAL: {real:.2f}\n"
                lista.append(f"XRP: {valor:.3f}\n")
                erro = 6
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
# ========================================================== #
def atualizar():
    moedas = open("moedas.txt", "r")
    lista2 = []
    for linha in moedas.readlines():
        ct = ""
        comeco = ""
        for i in range(9):
            comeco += linha[i]
        i = 9
        while linha[i] != " ":
            ct += linha[i]
            i += 1
        resto = ""
        while i != len(linha)-1:
            resto += linha[i]
            i += 1
        ct = float(ct)
        ct += ct*(randint(-5,5)/100)
        lista2.append(f"{comeco}{ct:.2f}{resto}\n")
    moedas.close()
    moedas = open("moedas.txt", "w")
    for i in range(len(lista2)):
        moedas.write(lista2[i])
    moedas.close()
# ========================================================== #
def extrato(cpf):
    extrato = open("extrato.txt","r")
    erro = 0
    nome = ""
    for linha in extrato.readlines():
        cpf1 = ""
        if erro == 0:
            for i in range(5,16):
                cpf1 += linha[i]
            if cpf1 == cpf:
                i = 23
                while i < len(linha)-1:
                    nome += linha[i]
                    i += 1
                erro = -1
            else:
                erro = 1
        elif erro == -1:
            if linha[0] != "\n":
                print(linha,end="")
            else:
                break
        else:
            erro += 1
            if linha[0] == "\n":
                erro = 0
    extrato.close()
# ========================================================== #
def menu(cpf):
    while True:
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
        id = int(input("Digite o numero da ação desejada: "))
        if id == 1:
            saldo(cpf)
        if id == 2:
            extrato(cpf)
        if id == 3:
            depositar(cpf)
        if id == 4:
            sacar(cpf)
        if id == 5:
            comprar(cpf)
        if id == 6:
            vender(cpf)
        if id == 7:
            atualizar()
        if id == 8:
            break

# ========================================================== #

while True:
    cpf = logar()
    menu(cpf)
