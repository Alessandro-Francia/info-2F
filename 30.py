lunghezza = int (input ("dimmi il numero delle cifre binarie"))
somma = 0
for n in range (lunghezza):
    cifra = int (input ("elenca le cifre a partire da destra"))
    valore = (cifra*2**n)
    somma += valore

print (somma)