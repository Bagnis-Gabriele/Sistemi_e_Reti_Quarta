"""
Bagnis Gabriele
LEARN PYTHON 3 THE HARD WAY capitolo 6
"""

#creo una variabile di tipo intero
types_of_people = 10
#creo una stringa inglobando al suo interno un'altra variabile
x = f"There are {types_of_people} types of people."

#creo due stringhe
binary = "binary"
do_not = "don't"
#creo una stringa composta da testo e dal contenuto di altre 2 stringhe
y = f"Those who know {binary} and those who {do_not}."  #posto 1-2

#stampo le due strighe precedentemente create
print(x)
print(y)

#stampo due stringhe che inglobano altre stringhe
print(f"I said: {x}")   #posto 3
print(f"I also said: '{y}'")    #posto 4

#creo due variabili, una è una domanda e l'altra rappresenta la risposta
hilarious = True
#le parentesi graffe indicano che in quel punto verrà poi aggiunta una stringa tramite il comando .format()
joke_evaluation = "Isn't that joke so funny?! {}"

#stampo la valutazione dello scherzo
print(joke_evaluation.format(hilarious))

#creo due stringhe
w = "This is the left side of..."
e = "a string with a right side."

#stampo le due stringhe concatenandole tramite la funzione dell'operatore polimorfo +
print(w + e)
#la stringa diventa più lunga perchè l'operatore + concatena 2 stringhe