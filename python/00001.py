"""
Bagnis Gabriele
Esercizio 1: chidere all'utente quanti elementi vuole inserire nella lista e poi inserirli chiedendoli all'utente
"""

dim = input("quanti numeri vuoi inserire?")
lista = []
for i in range(int(dim)):
    num = input("inserisci qualcosa")
    lista.append(num)
print(lista)