"""
Creare la matrice di un grafico orientato
"""
link = []
nodi = int(input("quanti nodi ci sono?")) + 1

#insert data
for k in range (1,nodi):
    node = []
    for i in range (0,nodi):
        data=2
        if k==1:
            data=1
        else:
            while data!=1 and data !=0:
                data= int(input(f"il nodo {k} è collegato al nodo {i}? (1 si, 0 no)"))
        node.append(data)
    link.append(node[:])
    
# drow matrix
for element in link:
    print(element)
