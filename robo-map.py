def ler_mapa(nome_ficheiro):
    mapa = []
    with open(nome_ficheiro, "r") as f:
        for linha in f:
            #remove espaços em branco nas extremidades
            #e divide a linha em elementos separados por espaços
            elementos = linha.strip().split()
            #para garantir que existe 10 elementos
            if len(elementos) == 10:
                mapa.append(elementos)
    mapa[0][0] = 'R'
    return mapa        

def menu(mapa):
        posX = 0
        posY = 0
                    
        while mapa[9][9] == ".":
            for linha in mapa:
                print(' '.join(linha))
            
            print("\nEscolha uma opção W,A,S,D para mover o Robot \nOpção 0 para encerrar o programa")
            opcao = input("Escolha uma opção: ")

            if opcao.lower() == "w" and posX > 0:
                posX -= 1
                if mapa[posX][posY] == "#":
                    print("\nFoste contra um obstáculo, tenta novamente1\n")
                    posX += 1
                else:
                    mapa[posX][posY] = "R"
                    
            elif opcao.lower() == "s" and posX < 9:
                posX += 1
                if mapa[posX][posY] == "#":
                    print("\nFoste contra um obstáculo, tenta novamente\n")
                    posX -= 1
                else:
                    mapa[posX][posY] = "R"
            elif opcao.lower() == "a" and posY > 0:
                posY -= 1
                if mapa[posX][posY] == "#":
                    print("\nFoste contra um obstáculo, tenta novamente\n")
                    posY += 1
                else:
                    mapa[posX][posY] = "R"
            elif opcao.lower() == "d" and posY < 9:
                posY += 1
                if mapa[posX][posY] == "#":
                    print("\nFoste contra um obstáculo, tenta novamente\n")
                    posY -= 1
                else:
                    mapa[posX][posY] = "R"              
            elif opcao == "0":
                print("Programa encerrado.")
                break
            else:
                print("\nOpção inválida. Tente novamente.\n")
                menu(mapa)
                
            if mapa[posX][posY] == mapa[9][9]:
                print("\n\nParabéns terminaste o jogo!!")
#executa o menu
print("O objetivo do jogo é chegar à saída no canto inferior direito\n")
menu(ler_mapa("mapa.txt"))

