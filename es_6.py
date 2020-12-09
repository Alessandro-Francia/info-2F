casuali = []
n = int (input ("quanti numeri ci devono essere da 1 a 20?"))
contatore = n
div = 2

for i in range (n):
    numero = randint (1,20)
    while numero in casuali:
        numero = randint (1,20)
    if numero not in casuali:
        casuali.append (numero)

print ("la lista è", casuali)

for numero in casuali:
    while True:
        if numero == div:
            div = 2
            break
        elif numero % div != 0:
            div += 1
        else:
            contatore -= 1
            div = 2
            break
print ("i numeri primi sono", contatore)