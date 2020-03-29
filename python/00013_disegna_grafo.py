"""
Disegnare un grafico basato su dati inseriti in input
"""
import networkx as nx
import matplotlib.pyplot as plt

def getData(v):
    data = {}
    for r in range(0, v):
        chiave = r + 1
        nod = [int(i) for i in input(f"Inserire i nodi vicini al nodo {chiave} (usare il '.' come separatore): ").split('.')]
        data[chiave] = nod
    return data

def disegnaGrafo(data):
    G = nx.Graph()
    for key, val in data.items():
        G.add_node(key)
        for i in val:
            G.add_edge(int(key), int(i))
    nx.draw(G)
    plt.show()

def stampaData(data):
    print("\n{")
    for key, val in data.items():
        print(f"\t{key}: {val},")
    print("}")

def main():
    v = int(input("Inserire il numero di nodi"))
    data = getData(v)
    stampaData(data)
    disegnaGrafo(data)

if __name__ == '__main__':
    main()