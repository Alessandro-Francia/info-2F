casuali = []
contatore = 0
n = int (input ("quanti numeri ci devono essere da 1 a 30?"))

for i in range (n):
    numero = randint (1,30)
    casuali.append (numero)
print ("la lista è", casuali)

for numero in casuali:
    if numero % 3 != 0:
        contatore += 1

print ("i numeri non divisibili per 3 sono", contatore)