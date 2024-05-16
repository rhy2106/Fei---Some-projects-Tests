def logar():
    while True:
        login = open("usuarios.txt", "r")
        cpf = input("Digite o seu CPF: ")
        senha = input("Digite a senha: ")
        linhas = login.readlines()
        for linha in linhas:
            cpf1 = linha[7:18]
            senha1 = linha[26:32]
            if cpf == cpf1 and senha == senha1:
                print("Login realizado com sucesso")
                login.close()
                return cpf
        print("login falhou, login ou senha errada")
        login.close()
# ========================================================== #
def verificarCpf(cpf,linha):
    return linha[5:16] == cpf
# ========================================================== #
def saldo(cpf):
    contas = open("contas.txt", "r")
    linhas = contas.readlines()
    i = 0
    while i < len(linhas):
        if not verificarCpf(cpf,linhas[i]):
            i += 6
            continue
        nome = linhas[i][23:-1]
        real = linhas[i+1][6:-1]
        btc = linhas[i+2][5:-1]
        eth = linhas[i+3][5:-1]
        xrp = linhas[i+4][5:-1]
        break
    contas.close()
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
    while True:
        real = float((input("Digite o valor em Real a ser depositado: ")))
        if real >= 0:
            break
        print("Valor Invalido")
    linhas = contas.readlines()
    i = 0
    while i < len(linhas):
        if not verificarCpf(cpf,linhas[i]):
            i += 6
            continue
        real += float(linhas[i+1][6:-1])
        linhas[i+1] = f"REAL: {real:.2f}\n"
        break
    contas = open("contas.txt", "w")
    for linha in linhas:
        contas.write(linha)
    contas.close()
# ========================================================== #
def sacar(cpf):
    contas = open("contas.txt", "r")
    linhas = contas.readlines()
    i = 0
    while i < len(linhas):
        if not verificarCpf(cpf,linhas[i]):
            i += 6
            continue
        real = float(linhas[i+1][6:-1])
        while True:
            real1 = float((input("Digite o valor em Real a ser sacado: ")))
            if real < real1:
                print("impossivel realizar esta ação")
            else:
                break
        real -= real1
        linhas[i+1] = f"REAL: {real:.2f}\n"
        contas.close()
        break
    contas = open("contas.txt", "w")
    for linha in linhas:
        contas.write(linha)
    contas.close()
# ========================================================== #
def comprar(cpf):
    moeda = input("Digite a moeda desejada (BTC, ETH ou XRP): ")
    contas = open("contas.txt", "r")
    moedas = open("moedas.txt", "r")
    linhas = contas.readlines()
    for linha in moedas.readlines():
        if (linha[0] == 'X' and moeda == "XRP")or(linha[0] == 'B' and moeda == "BTC")or(linha[0] == 'E' and moeda == "ETH"):
            l = linha.split(" ")
            txc = float(l[4])
            ct = float(l[2])
    moedas.close()
    i = 0
    while i < len(linhas):
        if not verificarCpf(cpf,linhas[i]):
            i += 6
            continue
        real = float(linhas[i+1][6:-1])
        while True:
            real1 = float((input("Digite o valor em reais da compra: ")))
            if real < real1:
                print("impossivel realizar esta ação, digite um novo valor:")
            else:
                break
        real -= real1
        linhas[i+1] =f"REAL: {real:.2f}\n"
        if moeda == "BTC":
            j = 2
        elif moeda == "ETH":
            j = 3
        elif moeda == "XRP":
            j = 4
        valor = (float(linhas[i+j][5:-1])) + (real1/ct)*(1-txc)
        linhas[i+j] = f"{moeda}: {valor:.3f}\n"
        break
    contas = open("contas.txt", "w")
    for linha in linhas:
        contas.write(linha)
    contas.close()
# ========================================================== #
def vender(cpf):
    moeda = input("Digite a moeda desejada (BTC, ETH ou XRP): ")
    contas = open("contas.txt", "r")
    moedas = open("moedas.txt", "r")
    linhas = contas.readlines()
    for linha in moedas.readlines():
        if (linha[0] == 'X' and moeda == "XRP")or(linha[0] == 'B' and moeda == "BTC")or(linha[0] == 'E' and moeda == "ETH"):
            l = linha.split(" ")
            txv = float(l[6])
            ct = float(l[2])
    moedas.close()
    i = 0
    while i < len(linhas):
        if not verificarCpf(cpf,linhas[i]):
            i += 6
            continue
        real = float(linhas[i+1][6:-1])
        if moeda == "BTC":
            j = 2
        elif moeda == "ETH":
            j = 3
        elif moeda == "XRP":
            j = 4
        valor = float(linhas[i+j][5:-1])
        while True:
            valor1 = float((input(f"Digite o valor em {moeda} da venda: ")))
            if valor < valor1:
                print("impossivel realizar esta ação, digite um novo valor:")
            else:
                valor -= valor1
                linhas[i+j] = f"{moeda}: {valor:.3f}\n"
                break
        real = real + valor1*ct - (real + valor1*ct)*txv
        linhas[i+1] = f"REAL: {real:.2f}\n"
        break
    contas = open("contas.txt", "w")
    for linha in linhas:
        contas.write(linha)
    contas.close()
# ========================================================== #
def atualizar():
    from random import randint
    moedas = open("moedas.txt", "r")
    linhas = moedas.readlines()
    i = 0
    while i < len(linhas):
        l = linhas[i].split(" ")
        ct = float(l[2])
        l[2] = f"{(ct + ct*(randint(-5,5)/100)):.2f}"
        linhas[i] = " ".join(l)
        i += 1
    moedas.close()
    moedas = open("moedas.txt", "w")
    for linha in linhas:
        moedas.write(linha)
    moedas.close()
# ========================================================== #
def extrato(cpf):
    extrato = open("extrato.txt","r")
    linhas = extrato.readlines()
    i = 0
    lista = []
    while i < len(linhas):
        if linhas[i] == "\n":
            lista.append(i)
        i += 1
    i = 0
    while i < len(linhas):
        if not verificarCpf(cpf,linhas[i]):
            i = lista[0] + 1
            lista.pop(0)
            continue
        nome = linhas[i][23:-1]
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        for i in range(i+1,len(linhas)):
            if linhas[i][0] != "\n":
                print(linhas[i],end="")
            else:
                break
        break
    extrato.close()
# ========================================================== #
def adicionarExtrato(cpf, moeda, acao):
    contas = open("contas.txt", "r")
    linhas = contas.readlines()
    i = 0
    while i < len(linhas):
        if not verificarCpf(cpf,linhas[i]):
            i += 6
            continue
        nome = float(linhas[i][23:-1])
        real = float(linhas[i+1][6:-1])
        btc = float(linhas[i+2][5:-1])
        eth = float(linhas[i+3][5:-1])
        xrp = float(linhas[i+4][5:-1])
        break
    contas.close()
    moedas = open("moedas.txt", "r")
    for linha in moedas.readlines():
        if (linha[0] == 'R' and moeda == "REAL")or(linha[0] == 'X' and moeda == "XRP")or(linha[0] == 'B' and moeda == "BTC")or(linha[0] == 'E' and moeda == "ETH"):
            l = linha.split(" ")
            if acao == "-":
                tx = float(l[6])
            elif acao == "+":
                tx = float(l[4])
            ct = float(l[2])
    moedas.close()
    
    from time import gmtime
    linhas = open("extrato.txt", "r")
    i = 0
    lista = []
    tempo = gmtime()
    while i < len(linhas):
        if linhas[i] == "\n":
            lista.append(i)
        i += 1
    i = 0
    while i < len(linhas):
        if not verificarCpf(cpf,linhas[i]):
            i = lista[0] + 1
            lista.pop(0)
            continue
	nome = linhas[i][23:-1]
	print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
	linhas.insert(i+1,f"{tempo.tm_mday}-{tempo.tmon}-{tempo.year} {tempo.tm_hour - 3}:{tempo.tm_min} {acao} {moeda} CT: {ct} TX: {tx} REAL: {real} BTC: {btc} ETH: {eth} XRP: {xrp}\n")
        for i in range(i+1,len(linhas)):
            if linhas[i][0] != "\n":
                print(linhas[i],end="")
            else:
                break
        break
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
