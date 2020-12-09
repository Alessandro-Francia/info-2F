multipli = []
multipli_2 = []
n = int (input ("quanti multipli di 10 vuoi inserire?"))
for i in range (1,n+1):
    multipli.append (10*i)

print (multipli)

for elemento in multipli:
    if elemento <= 30:
        multipli_2.append (elemento)
    else:
        multipli_2.append (int (elemento/2))

print ("la nuova lista è ", multipli_2)