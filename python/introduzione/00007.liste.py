lista=[1,2,3]
print(lista)
posizione=1

for i in lista:
    print(i)    #i è l'elemento della lista

lista[posizione]        #mi restituisce l'elemeto nella posizione
lista[-1]               #mi restituisce l'ultimo elemento (-2 penultimo e così via)
lista[3:5]  #elementi dall'elemento 3 al 4 (5 è escluso) -slicing
lista[3:]    #elementi dal terzo fino alla fine 
lista[::2]  #mi restituisce un elemento ogni due 

lista.append(1) #aggiunge l'elemento alla lista

elemento=2
lista.remove(elemento)  #elimina la prima occorrenza dell'elemento
lista.pop() #se tra parentesi metto la posizione di un un'elemento ne fa la pop altrimenti estrae l'ultimo
lista.count(elemento)   #conta quante volte si ripete un'elemento

lista.sort()    #ordina la lista
lista.reverse() #inverte la stringa

len(lista)  #restituisce la lunghezza della lista

l2=lista   #puntano alla stessa area di memoria
l3=lista.copy() #copia tutti gli elementi

lista.copy()