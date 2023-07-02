import sys
mapa =[['O', '=', '=', '+', '=', '=', '=', '=', '=', '1'], ['^', '#', '#', 'v', '#', '#', '#', '#', '#', '"'], ['^', '#', '#', 'v', '#', '#', '#', '#', '#', '"'], ['^', '#', '#', 'v', '#', '#', '#', '#', '#', '"'], ['^', '#', '#', '+', '=', '=', '=', '=', '=', '+'], ['^', '#', '#', 'v', '#', '#', '#', '#', '#', '"'], ['^', '#', '#', 'v', '#', '#', '#', '#', '#', '"'], ['^', '#', '#', 'v', '#', '#', '#', '#', '#', '"'], ['^', '#', '#', 'v', '#', '#', '#', '#', '#', '"'], ['^', '<', '<', '2', '<', '<', '<', '<', '<', '+']]

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
    for i in range(0,10):
        line = ""
        for j in range(0,10):
            if(posicao==0):
                line = line + (mapa[i][j])
            else:
                if(posicao[0]!=i or posicao[1]!=j):
                    line = line + (mapa[i][j])
                else:
                    line = line + "@"
        print(line)

def posicaoInicial():
    initial = int(input("Escolha onde Iniciar (1 ou 2): \n"))
    while(initial >2 or initial <1):
        initial = int(input("Escolha onde Iniciar (1 ou 2): \n"))
    if(initial == 1):
        posicao= [0,9]
    elif(initial == 2):
        posicao=[9, 3]
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
        if(int(posicao[0]) < 0 or int(posicao[0]) > 9 or int(posicao[1]) < 0 or int(posicao[1]) > 9):
            return True
        else:
            return False
    else:
        if(int(posicao[0]) < 0 or int(posicao[0]) > 9 or int(posicao[1]) < 0 or int(posicao[1]) > 9):
            print("\n" * 100)
            print("Você saiu da cidade, fim de jogo")
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
        return False
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
        print("\n" * 100)
        printarMapa(posicaoAtual)
        movimentacao = input("Para onde ir?")
    posicaoFutura = validarMovimento(movimentacao, posicaoAtual)
    if(foraLimite(posicaoFutura, posicaoAtual)):
        print("\n" * 100)
        print("Você saiu do mapa")
        continuar = input("Pressione enter para sair")
        sys.exit()
    else:
        if(validaColisao(posicaoFutura)):
            print("\n" * 100)
            print("Você colidiu com um objeto, você perdeu");
            continuar = input("Pressione enter para sair")
            sys.exit()
        else:
            if(validaDirecao(movimentacao, posicaoAtual)):
                print("\n" * 100)
                print("Movimento invalido, siga o curso da via")
                continuar = input("Pressione enter para continuar")
            else:
                posicaoAtual = posicaoFutura