"""
Bagnis Gabriele
Esercizio 4: Sorteggiatore di alunni per l'interrogazione
"""
import random
nameList = ["Mario Rossi", "John Doe", "Tizio Caio"]

for num, student in enumerate(nameList):
    print(f"{num} - {student}")

print("oggi viene interrogato: " + nameList[(random.randint(0,len(nameList)-1))])
