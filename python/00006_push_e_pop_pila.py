"""
Bagnis Gabriele
Esercizio 6: Implementare i metodi pop e push della pila
"""

def push(stack, element):
    stack.append(element)
    return stack

def pop(stack):
    element = stack.pop()
    return stack, element

pila = [1,2,3,4,"stack"]

pila = push(pila, "ciao")

print(pila)
pila,_= pop(pila)
print(pila)
