"""
Bagnis Gabriele
Esercizio 3: date 2 liste creare una 3 lista con solo gli elementi in comune
"""

lista1 = [1,2,3,4,5,6,7,8,9,0]
lista2 = [33,55,66,77,88,99,0,1,2]
lista3 = []
for i in lista1:
    if i in lista2:
        lista3.append(i)
print(lista3)
