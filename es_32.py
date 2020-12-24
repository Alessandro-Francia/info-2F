'''
implementa l'algoritmo per il calcolo della soluzione
di un'equazione di primo grado ax + b = 0.
'''

print ("inserie a e b per risolvere l'equazione ax + b = 0")
a = int (input ())
b = int (input ())

if a == 0 and b == 0:
    print ("equazione indeterminata")
elif a == 0 and b != 0:
    print ("equazione impossibile")
else:
    x = int (-b/a)
    print ("il valore di x è:", x)