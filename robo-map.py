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
posX = 0
posY = 0
totalM = 0

def moveUp(mapa):
    #se existir o ponto trocar por R
    if mapa[posX - 1][posY] == '.':
        mapa[posX - 1][posY] = 'R'
    #caso contrário damos erro e voltamos para trás
    elif mapa[posX - 1][posY] == '#':
        print("Existe um obstáculo!")
    elif mapa[posX - 1][posY] == 'R':
        print("Estás a voltar para trás!")
    else:
        print("Não podes sair do mapa!")

def moveDown(mapa):
    #se existir o ponto trocar por R
    if mapa[posX + 1][posY] == '.':
        mapa[posX + 1][posY] = 'R'
    #caso contrário damos erro e voltamos para trás
    elif mapa[posX + 1][posY] == '#':
        print("Existe um obstáculo!")
    elif mapa[posX + 1][posY] == 'R':
        print("Estás a voltar para trás!")
    else:
        print("Não podes sair do mapa!")

def menu():
        mapa = ler_mapa("mapa.txt")
            
        while True:
            for linha in mapa:
                print(' '.join(linha))
            
            print("\nEscolha uma opção W,A,S,D para mover o Robô \nOpção 0 para encerrar o programa")
            opcao = input("Escolha uma opção: ")

            if opcao.lower() == "w":
                moveUp(mapa)
            elif opcao.lower() == "a":
                #moveLeft(mapa)
                print("Hello")
            elif opcao.lower() == "s":   
                moveDown(mapa) 
            elif opcao.lower() == "d":
                #moveRight(mapa) 
                print("Hello")
                      
            elif opcao == "0":
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida. Tente novamente.")
                menu()
#executa o menu
menu()