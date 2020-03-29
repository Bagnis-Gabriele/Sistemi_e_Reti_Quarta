"""
Creare la matrice di un grafico orientato e pesato
"""
def MatricePesataOrientata():
    nodi = int(input("Inserire numero di nodi: "))
    matrice = []

    for i in range(0,nodi):
        nodi_pesati = [elemento for elemento in input(f"Inserisci i nodi adiacenti a {i} con il peso (nodo|peso,nodo|peso): ").split(",")]
        riga = [0 for elemento in range(0,nodi)]
        nodi_vicini=[]
        pesi=[]
            
        for i in nodi_pesati:
            n,p = i.split("|")
            nodi_vicini.append(int(n))
            pesi.append(int(p))
        print(nodi_vicini,pesi)
        for p,n in enumerate(nodi_vicini):
            riga[n] = pesi[p]

        matrice.append(riga)
    return matrice

def main():
    m = MatricePesataOrientata()
    for element,_ in enumerate(m):
        print(m[element])

if __name__ == "__main__":
    main()