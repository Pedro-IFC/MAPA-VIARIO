import sys
mapa =[['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '1', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'O', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ''], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'v', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '^', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ''], ['2', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '+', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '^', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ''], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'v', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ''], ['O', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '<', '+', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '+', '=', '=', '=', '=', '=', '=', 'X', ''], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '^', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '^', '<', '<', '<', '<', '<', '<', '3', ''], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '^', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ''], ['4', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '+', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '+', '>', '>', '>', '>', '>', '>', '>', '>', '>', 'o'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'v', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'v', '#', '#', '#', '#', '#', '#', '#', '#', '#', ''], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', 'v', '#', '#', '#', '#', '#', '#', '#', '#', '#', ''], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'v', '#', '#', '#', '#', '#', '#', '#', '#', '#', ''], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'v', '#', '#', '#', '#', '#', '#', '#', '#', '#', ''], ['5', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', 'v', '#', '#', '#', '#', '#', '#', '#', '#', '#', ''], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '>', '>', '>', '>', '>', '>', '>', '>', '>', 'O', '']]

def printarComandos():
    print("==============================================================")
    print("D -Para direita")
    print("A -Para esquerda")
    print("W -Para cima")
    print("S -Para baixo")
    print("Para sair aperte ctrl + C")
    print("==============================================================")

def printarMapa(posicao=0):
    print("Mapa:")
    print("==============================================================\n")
    for i in range(len(mapa)):
        line=""
        for j in range(len(mapa[i])):
            if(posicao==0):
                line = line + (mapa[i][j])
            else:
                if(posicao[0]!=i or posicao[1]!=j):
                    line = line + (mapa[i][j])
                else:
                    line = line + "@"
        print(line)

def posicaoInicial():
    initial = int(input("Escolha onde Iniciar (1,2,3,4 ou 5): \n"))
    while(initial >5 or initial <1):
        initial = int(input("Escolha onde Iniciar (1,2,3,4 ou 5): \n"))
    if(initial == 1):
        posicao= [0,30]
    elif(initial == 2):
        posicao=[2, 0]
    elif(initial == 3):
        posicao=[5, 60]
    elif(initial == 4):
        posicao=[7, 0]
    elif(initial == 5):
        posicao=[12, 0]
    return posicao

def validarMovimento(movimentacao, posicaoAtual):
    if(movimentacao == 'd'):
        posicaoFutura = [int(posicaoAtual[0]), int(posicaoAtual[1])+1]
    elif(movimentacao == 'a'):
        posicaoFutura = [int(posicaoAtual[0]), int(posicaoAtual[1])-1]
    elif(movimentacao == 's'):
        posicaoFutura = [int(posicaoAtual[0])+1, int(posicaoAtual[1])]
    elif(movimentacao == 'w'):
        posicaoFutura = [int(posicaoAtual[0])-1, int(posicaoAtual[1])]
    else:
        posicaoFutura = posicaoAtual
    return posicaoFutura

def foraLimite(posicao, posicaoAtual):
    if(mapa[posicaoAtual[0]][posicaoAtual[1]]!="O"):
        if(int(posicao[0]) < 0 or int(posicao[0]) > 13 or int(posicao[1]) < 0 or int(posicao[1]) > 60):
            return True
        else:
            return False
    else:
        if(int(posicao[0]) < 0 or int(posicao[0]) > 9 or int(posicao[1]) < 0 or int(posicao[1]) > 9):
            print("\n" * 100)
            print("Você saiu da cidade")
            continuar = input("Pressione enter para sair")
            sys.exit()
        else:
            return False

def validaColisao(posicaoFutura):
    if(mapa[posicaoFutura[0]][posicaoFutura[1]]=="#"):
        return True
    else:
        return False

def validaDirecao(movimentacao, posicaoAtual):
    if(mapa[posicaoAtual[0]][posicaoAtual[1]]=="2"):
        if(movimentacao == "a"):
            return False
        else:
            return True
    elif(mapa[posicaoAtual[0]][posicaoAtual[1]]=="1"):
        if(movimentacao == "s" or movimentacao == "a"):
            return False
        else:
            return True
    elif(mapa[posicaoAtual[0]][posicaoAtual[1]]=="O"):
        if(movimentacao == "d"):
            return False
        else:
            return True
    elif(mapa[posicaoAtual[0]][posicaoAtual[1]]=="<"):
        if(movimentacao == "a"):
            return False
        else:
            return True
    elif(mapa[posicaoAtual[0]][posicaoAtual[1]]==">"):
        if(movimentacao == "d"):
            return False
        else:
            return True
    elif(mapa[posicaoAtual[0]][posicaoAtual[1]]=="v"):
        if(movimentacao == "s"):
            return False
        else:
            return True
    elif(mapa[posicaoAtual[0]][posicaoAtual[1]]=="^"):
        if(movimentacao == "w"):
            return False
        else:
            return True
    elif(mapa[posicaoAtual[0]][posicaoAtual[1]]=="="):
        if(movimentacao == "a" or movimentacao =="d"):
            return False
        else:
            return True
    elif(mapa[posicaoAtual[0]][posicaoAtual[1]]=="+"):
        futuro = validarMovimento(movimentacao, posicaoAtual)
        futuro2 = validarMovimento(movimentacao, futuro)
        if(foraLimite(futuro, futuro2)):
            return True
        elif(validaColisao(futuro)):
            return True
        else:
            if(mapa[futuro[0]][futuro[1]]=="<"):
                if(movimentacao == "a"):
                    return False
                else:
                    return True
            elif(mapa[futuro[0]][futuro[1]]==">"):
                if(movimentacao == "d"):
                    return False
                else:
                    return True
            elif(mapa[futuro[0]][futuro[1]]=="v"):
                if(movimentacao == "s"):
                    return False
                else:
                    return True
            elif(mapa[futuro[0]][futuro[1]]=="^"):
                if(movimentacao == "w"):
                    return False
                else:
                    return True
            elif(mapa[futuro[0]][futuro[1]]=="="):
                if(movimentacao == "a" or movimentacao =="d"):
                    return False
                else:
                    return True
    elif(mapa[posicaoAtual[0]][posicaoAtual[1]]=='"'):
        if(movimentacao == "w" or movimentacao =="s"):
            return False
        else:
            return True
    else:
        return False

print("\n" * 100)
printarComandos()
continuar = input("Pressione enter para continuar")
if(continuar is not None):
    print("\n" * 100)
    printarMapa()
    posicaoAtual = posicaoInicial()

while(True):
    print("\n" * 100)
    printarMapa(posicaoAtual)
    movimentacao = input("Para onde ir?")
    while(validarMovimento(movimentacao, posicaoAtual)==posicaoAtual):
        print("\n" * 100)
        print("Comando errado, tente novamente")
        continuar = input("Pressione enter para tentar novamente")
        print("\n" * 100)
        printarMapa(posicaoAtual)
        movimentacao = input("Para onde ir?")
    posicaoFutura = validarMovimento(movimentacao, posicaoAtual)
    if(foraLimite(posicaoFutura, posicaoAtual)):
        print("\n" * 100)
        print("Você sairá do mapa, tente novamente")
        continuar = input("Pressione enter para tentar novamente")
    else:
        if(validaColisao(posicaoFutura)):
            print("\n" * 100)
            print("Você colidiu com um objeto, tente novamente");
            continuar = input("Pressione enter para tentar novamente")
        else:
            if(validaDirecao(movimentacao, posicaoAtual)):
                print("\n" * 100)
                print("Movimento invalido, siga o curso da via")
                continuar = input("Pressione enter para continuar")
            else:
                posicaoAtual = posicaoFutura