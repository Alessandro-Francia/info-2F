'''
Dato un elenco di studenti di partecipanti a una gara sportiva di lancio del peso (nome studente, lancio),
visualizza il valore del lancio del vincitore (valore massimo).
'''

valori= []
print ("rispondi 0 al punteggio se hai finito")

while True:
    nome = input ("nome studente")
    punteggio = int (input ("quanti punti ha fatto?"))
    if punteggio == 0:
        break
    valori.append(punteggio)

print (max (valori))