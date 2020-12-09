A = []
B = []
while True:
    parola = input ("aggiungi una parola alla lista")
    A.append (parola)
    fine = int (input ("premi 0 per uscire, altrimenti premi qualsiasi altro numero"))
    if fine == 0:
        break
for i in A:
    lunghezza = len (i)
    B.append (lunghezza)
print (B)