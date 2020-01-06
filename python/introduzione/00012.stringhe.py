astring = "Hello world!"
print("single quotes are ' '")  

print(len(astring)) #calcola la lunghezza di una stringa

astring = "Hello world!"
print(astring.index("o"))   #stampa la posizione della prima ricorrenza uguale a quella inserita

astring = "Hello world!"
print(astring.count("l"))   #restituisce il numero di ricorrenze

astring = "Hello world!"
print(astring[3:7])     #stampa i caratteri dal terzo al settimo elemento

astring = "Hello world!"
print(astring[3:7:2])   #stampa un carattere ogni due dal terzo al settimo elemento

astring = "Hello world!"
print(astring[::-1])    #ribalta la stringa

astring = "Hello world!"
print(astring.upper())  #tutti i caratteri diventano maiuscoli
print(astring.lower())  ##tutti i caratteri diventano minuscoli

astring = "Hello world!"
print(astring.startswith("Hello"))      #controlla se la stringa comincia con quei caratteri
print(astring.endswith("asdfasdfasdf")) #controlla se la stringa termina con quei caratteri

astring = "Hello world!"
afewwords = astring.split(" ")  #divide la stringa a ogni occorrenza di questo carattere restituendole come un vettore di stringhe