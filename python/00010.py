"""
Dati in input i nodi e i link dei grafo, disegnarlo
"""
def main():
    link = []
    node = []

    #insert data
    while (input("1 per inserire un altro dato")==1):
        node1=input("inserisci il nodo 1")
        node2=input("inserisci il nodo 2")
        link.append([node1,node2])
        presente=0
        for element in node:
            if element == node1:
                presente=1
        if(presente==0):
            node.append(node1)
        presente=0
        for element in node:
            if element == node2:
                presente=1
        if(presente==0):
            node.append(node2)
        node.sort()

    #create matrix
        
    
#this function is used to convert the program into a library in case you want to use it in that way
if __name__ == "__main__":
    main()