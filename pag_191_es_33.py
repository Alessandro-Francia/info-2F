'''
In un laboratorio di analisi i pazienti sono sottoposti a un esame specialistico secondo l'ordine di arrivo:
scrivi il programma che consenta di registrare i nomi dei pazienti man mano che arrivano.
Visualizza poi il nome del paziente che deve essere sottoposto all'esame perchè è il primo della coda in attesa.
'''

coda = []

while True:
    print ("inserire i pazienti in ordine di arrivo, non inserire nulla per smettere di inserire i nomi:")
    nome = input ("")
    if nome != "":
        coda.append (nome)
    else:
        break

print ("il primo paziente da sottoporre all'esame è", coda [0])