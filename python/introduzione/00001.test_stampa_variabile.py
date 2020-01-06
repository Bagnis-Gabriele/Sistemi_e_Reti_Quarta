x=10
print(f"x vale: {x}")

# la stampa può funzionare anche in modo molto simie al c
name = "John"
age = 23
print("%s is %d years old." % (name, age))

#con questo linguaggio è molto più semplice stampare un vettore
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)