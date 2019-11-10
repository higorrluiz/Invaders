def adicionar_jogador():
    nome=input("Digite seu nome: ")
    arquivo=open("ranking.txt","a")
    arquivo.write(nome + " " + str(int(score)) + "\n")
    arquivo.close()

def ordenar_ranking():
    arquivo = open("ranking.txt","r")
    lista = arquivo.readlines()
    pontuação=[]
    nomes=[]
    for i in range(len(lista)):
        aux= lista[i].split()
        pontuação.append(int(aux[1]))
        nomes.append(aux[0])

    for i in range(1,len(pontuação)):
        for j in range(len(pontuação)-1):
            if pontuação[j] < pontuação[j+1]:
                pontuação[j],pontuação[j+1] = pontuação[j+1],pontuação[j]
                nomes[j],nomes[j+1] = nomes[j+1],nomes[j]
    arquivo.close()
    arquivo = open("ranking.txt","w")

    for i in range(len(nomes)):
        arquivo.write(nomes[i] + " " + str(pontuação[i]) + "\n")

    arquivo.close()

def contar_pessoas():
    arquivo = open("ranking.txt","r")
    lista = arquivo.readlines()
    arquivo.close()
    return lista
