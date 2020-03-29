"""
Creare la matrice di un grafico orientato
"""
def MatriceOrientata():
    nodi = int(input("Inserire numero di nodi: "))
    matrice = []

    for i in range(0,nodi):
        data = [elemento for elemento in input(f"Inserisci i nodi adiacenti a {i} (nodo,nodo): ").split(",")]
        riga = [0 for elemento in range(0,nodi)]
        nodi_vicini=[]
            
        for i in data:
            nodi_vicini.append(int(i))
        print(nodi_vicini)
        for i in range(0,nodi):
            for k in nodi_vicini:
                if(i==k):
                    riga[i]=1

        matrice.append(riga)
    return matrice

def main():
    m = MatriceOrientata()
    for element,_ in enumerate(m):
        print(m[element])

if __name__ == "__main__":
    main()