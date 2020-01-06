"""
Bagnis Gabriele
Esercizio 7: Correzione della verifica
"""

import random

"""
classi: carta
"""
#creazione della struttura
class carta(object):
    def __init__(self, seme, numero):
        self.seme = seme
        self.numero = numero
    def stampa(self):
        print(f"la carta ha seme {self.seme} con numero {self.numero}")

"""
funzioni: push, pop, coppaMazzo
"""
#funzione push della pila
def push(stack, element):
    stack.append(element)
    return stack

#funzione pop della pila
def pop(stack):
    element = stack.pop()
    return stack, element

def coppaMazzo(stack):
    pos=random.randint(0,len(stack)-1)
    stack = stack[pos:len(stack)] + stack[0:pos]
    return stack

def mischiaMazzo(stack):
    stack1=[]
    while stack!=[]:
        stack=coppaMazzo(stack)
        stack1.append(stack.pop())
    return stack1

"""
Codice
"""

Mazzo = []
Semi = ["C","Q","F","P"]

for i in range (1,14):
    for s in Semi:
        push(Mazzo, carta(s,i))

for i in Mazzo:
    i.stampa()

Mazzo=coppaMazzo(Mazzo)

print("\n\nmazzo coppato:\n")

for i in Mazzo:
    i.stampa()

Mazzo=mischiaMazzo(Mazzo)

print("\n\nmazzo mischiato:\n")

for i in Mazzo:
    i.stampa()
