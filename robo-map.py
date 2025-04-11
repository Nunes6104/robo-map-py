import os
import shutil
file = "test.txt"
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
    mapa[0][0][0] == 'R'
    return mapa

def moveUp(mapa):
    if True:
        for el in mapa:
            print(' '.join(el))
            

def moveDown():
    print("hello")
    
def moveLeft():
    print("hello")
    
def moveRight():
    print("hello")

def menu():
    if os.path.exists(file):
        mapa = ler_mapa(file)
        while True:
            print("Escolha uma opção W,A,S,D para mover o Robô \nOpção 0 para encerrar o programa")
            opcao = input("Escolha uma opção: ")

            if opcao.lower() == "w":
                moveUp(mapa)
            elif opcao.lower() == "a":
                moveLeft()
            elif opcao.lower() == "s":
                moveDown()                
            elif opcao.lower() == "d":
                moveRight()                
            elif opcao == "0":
                print("Programa encerrado.")
                os.remove(file)
                break
            else:
                print("Opção inválida. Tente novamente.")
                menu()
    else:
        shutil.copy("mapa.txt", file)
        menu()
#executa o menu
menu()