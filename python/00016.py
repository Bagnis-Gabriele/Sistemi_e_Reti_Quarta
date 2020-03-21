"""
Robot e Grafi (dizionario)
"""

def DizionarioDaMatrice(matrice):

    #funzione che numera le caselle esistenti della matrice a partire da 1
    n_nodi = 1
    for r in range(0,len(matrice)):
        for c in range(0,len(matrice)):
            if matrice[r][c]:
                matrice[r][c] = n_nodi
                n_nodi = n_nodi + 1

    d = {}
    n_nodi = 1
    ponti =[]

    for r in range(0,len(matrice)):
        for c in range(0,len(matrice)):
            ponti= []
            if matrice[r][c]!= False:
                if r-1 >= 0:
                    if(matrice[r-1][c]!=False):
                        ponti.append(matrice[r-1][c])
                if c-1 >= 0:
                    if(matrice[r][c-1]!=False):
                        ponti.append(matrice[r][c-1])
                if c+1 < len(matrice):
                    if(matrice[r][c+1]!=False):
                        ponti.append(matrice[r][c+1])
                if r+1 < len(matrice):
                    if(matrice[r+1][c]!=False):
                        ponti.append(matrice[r+1][c])

                d[n_nodi] = ponti
                n_nodi =n_nodi+1
                print(ponti)
    
    return d

    
    

griglia = [[True, True, True, True, True, False],
        [False, False, True, True, True, False],
        [True, True, True, False, True, True],
        [True, False, False, True, True, False],
        [True, True, True, True, False, True],
        [True, False, True, True, True, False]]

print(DizionarioDaMatrice(griglia))