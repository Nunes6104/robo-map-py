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
    return mapa

def mostrar_mapa(mapa):
    print("\nMapa Original:")
    for linha in mapa:
        print(' '.join(linha))

def mostrar_mapa_codificado(mapa):
    print("\nMapa Codificado (~ para '.', X para '#'):")
    for linha in mapa:
        linha_codificada = ['~' if c == '.' 
                            else 'X' 
                            for c in linha]
        print(' '.join(linha_codificada))

def buscar_mapa(mapa):
    print("\nPosições dos obstáculos (#):")
    total = 0
    for i in range(10):
        for j in range(10):
            if mapa[i][j] == '#':
                print(f"Obstáculo em: [{i}, {j}]")
                total += 1
    print(f"Total de obstáculos: {total}")

def menu():
    mapa = ler_mapa("proj1/mapa.txt")
    while True:
        print("\nMenu de Opções:")
        print("1 - Mostrar mapa original")
        print("2 - Mostrar mapa com substituições (~ e X)")
        print("3 - Mostrar posições dos obstáculos e total")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_mapa(mapa)
        elif opcao == "2":
            mostrar_mapa_codificado(mapa)
        elif opcao == "3":
            buscar_mapa(mapa)
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu principal
menu()
