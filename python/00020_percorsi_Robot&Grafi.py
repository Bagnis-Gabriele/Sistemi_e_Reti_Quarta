"""
percorso robot e grafi
"""

def dijkstra(matrice,node):
    if len(matrice)-1 < node:
        print("Non esiste il nodo inserito")
        return 0;
    percorsi={}
    predecessori={}
    nodi_disponibili=[]
    cont=0
    for i in range(0,len(matrice)):
        nodi_disponibili.append(cont)
        percorsi[str(cont)]=-1
        predecessori[str(cont)]="non presente"
        cont += 1

    nodo = node
    percorsi[str(node)]=0
    predecessori[str(node)]=str(nodo)
    end=True
    while len(nodi_disponibili)!=0 and end:
        for nr,_ in enumerate(matrice):
            if matrice[nodo][nr] > -1:
                if percorsi[str(nr)] > percorsi[str(nodo)]+matrice[nodo][nr] or percorsi[str(nr)]==-1:
                    percorsi[str(nr)]=percorsi[str(nodo)]+matrice[nodo][nr]
                    predecessori[str(nr)]=str(nodo)
        nodi_disponibili.remove(nodo)
        nodo_p=nodo
        min=9999
        for i in nodi_disponibili:
            if percorsi[str(i)] > -1:
                if percorsi[str(i)] < min:
                    nodo = i
                    min = percorsi[str(i)]
        if nodo == nodo_p:
            end=False
    return percorsi, predecessori

def generaScacchiera():
    scacchiera = []
    dim = int(input("Inserisci la dimensione della scacchiera: "))
    for i in range(0, dim):
        riga = []
        for j in range(0, dim):
            riga.append(1)
        scacchiera.append(riga)
    ancora = int(input("ci sono ostacoli? (0 per no)"))
    while ancora != 0:
        ostacolo = input("Inserisci le cordinate della cella con ostacolo (x.y) ")
        cordinate = ostacolo.split(".")
        scacchiera[int(cordinate[1])][int(cordinate[0])] = 0
        ancora= int(input("c'è n'è ancora? (0 per terminare)"))
    
    return scacchiera

def MatriceAdiacenzeDaMatrice(matrice):
    #funzione che numera le caselle esistenti della matrice a partire da 1
    n_nodi = 1
    for r in range(0,len(matrice)):
        for c in range(0,len(matrice)):
            if matrice[r][c]:
                matrice[r][c] = n_nodi
                n_nodi = n_nodi + 1

    #crea una matrice di adiacenze considerando solo i nodi esistenti
    adiacenze = []
    for r in range(0,n_nodi-1):
        riga =[]
        for c in range(0,n_nodi-1):
            riga.append(-1)
        adiacenze.append(riga)

    for r in range(0,len(matrice)):
        for c in range(0,len(matrice)):
            if matrice[r][c]!= 0:
                if r-1 >= 0:
                    if(matrice[r-1][c]!=0):
                        adiacenze[int(matrice[r][c])-1][int(matrice[r-1][c])-1]=1
                        adiacenze[int(matrice[r-1][c])-1][int(matrice[r][c])-1]=1
                if c-1 >= 0:
                    if(matrice[r][c-1]!=0):
                        adiacenze[int(matrice[r][c])-1][int(matrice[r][c-1])-1]=1
                        adiacenze[int(matrice[r][c-1])-1][int(matrice[r][c])-1]=1
                if c+1 < len(matrice):
                    if(matrice[r][c+1]!=0):
                        adiacenze[int(matrice[r][c])-1][int(matrice[r][c+1])-1]=1
                        adiacenze[int(matrice[r][c+1])-1][int(matrice[r][c])-1]=1
                if r+1 < len(matrice):
                    if(matrice[r+1][c]!=0):
                        adiacenze[int(matrice[r][c])-1][int(matrice[r+1][c])-1]=1
                        adiacenze[int(matrice[r+1][c])-1][int(matrice[r][c])-1]=1
    
    return adiacenze


def main():
    scacchiera = []
    scacchiera = generaScacchiera()
    adiacenze = []
    adiacenze = MatriceAdiacenzeDaMatrice(scacchiera)
    predecessori = {}
    distanze = {}
    repeat=1
    while repeat:
        posizione = input("inserisci le coordinate del nodo (x.y)")
        node = posizione.split(".")
        if scacchiera[int(node[1])][int(node[0])] != 0:
            nodo = scacchiera[int(node[1])][int(node[0])] -1
            repeat=0
        else:
            repeat=1
    distanze, predecessori = dijkstra(adiacenze,nodo)
    i=0
    for _ in distanze:
        print(f"nodo {i}:\n\tdistanza: {distanze[str(i)]}\n\tpredecessore: {predecessori[str(i)]}")
        i+=1
    
if __name__ == "__main__":
    main()