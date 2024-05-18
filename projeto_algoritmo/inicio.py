def adicionarExtrato(cpf, moeda, acao, valor):
    contas = open("contas.txt", "r")
    linhas = contas.readlines()
    i = 0
    while i < len(linhas):
        if not verificarCpf(cpf,linhas[i]):
            i += 6
            continue
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
    extrato = open("extrato.txt","r")
    linhas = extrato.readlines()
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
        hora = tempo.tm_hour-3
        if hora < 0:
            hora = 24 - hora
        tempo = f"{tempo.tm_mday:0>2}-{tempo.tm_mon:0>2}-{tempo.tm_year} {(hora):0>2}:{tempo.tm_min:0>2}"
        linhas.insert(i+1,f"{tempo} {acao} {valor} {moeda} CT: {ct} TX: {tx} REAL: {real} BTC: {btc} ETH: {eth} XRP: {xrp}\n")
        break
    extrato.close()
    extrato = open("extrato.txt","w")
    for linha in linhas:
        extrato.write(linha)
    extrato.close()
# ========================================================== #
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
        v = real
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
    adicionarExtrato(cpf, "REAL", "+", v)
    saldo(cpf)
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
                v = real1
                break
        real -= real1
        linhas[i+1] = f"REAL: {real:.2f}\n"
        contas.close()
        break
    contas = open("contas.txt", "w")
    for linha in linhas:
        contas.write(linha)
    contas.close()
    saldo(cpf)
    adicionarExtrato(cpf, "REAL", "-", v)
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
            if real < real1 + real1*txc:
                print("impossivel realizar esta ação, digite um novo valor:")
            else:
                v = real1
                break
        real -= (real1 + real1*txc)
        linhas[i+1] =f"REAL: {real:.2f}\n"
        if moeda == "BTC":
            j = 2
        elif moeda == "ETH":
            j = 3
        elif moeda == "XRP":
            j = 4
        valor = (float(linhas[i+j][5:-1])) + (real1/ct)
        linhas[i+j] = f"{moeda}: {valor:.3f}\n"
        break
    contas = open("contas.txt", "w")
    for linha in linhas:
        contas.write(linha)
    contas.close()
    saldo(cpf)
    adicionarExtrato(cpf, moeda, "+", v)
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
        v = valor1*ct - (valor1*ct)*txv
        real = real + v
        linhas[i+1] = f"REAL: {real:.2f}\n"
        break
    contas = open("contas.txt", "w")
    for linha in linhas:
        contas.write(linha)
    contas.close()
    saldo(cpf)
    adicionarExtrato(cpf, moeda, "-", f"{v:.2f}")
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
        val_tamanho = []
        for j in range(i+1,len(linhas)):
            if linhas[j][0] == "\n":
                break
            linha = linhas[j].split(" ")
            for o in range(len(linha)):
                if j == i + 1:
                    val_tamanho.append(len(linha[o]))
                else:
                    if val_tamanho[o] < len(linha[o]):
                        val_tamanho[o] = len(linha[o])
        for j in range(i+1,len(linhas)):
            if linhas[j][0] == "\n":
                break
            linha = linhas[j].split(" ")
            for o in range(len(linha)):
                a = val_tamanho[o]
                print(f"{linha[o]:<{a}}",end="")
                if linha[j+1][0] == "\n" or o == len(linha)-1:
                    break
                print(" ",end="")
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
