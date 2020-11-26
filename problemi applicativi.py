programma =int (input ("quale dei 4 programmi vuoi correggere?"))

if programma == 1:

    voto1 = int (input ("dimmi il voto del primo candidato"))
    voto2 = int (input ("dimmi il voto del secondo"))
    totale = voto1+voto2
    if voto1 > voto2:
        voto1 = voto1*100
        percentuale = voto1/totale
        print ("il primo ha vinto con", percentuale, "% dei voti")
    elif voto2 > voto1:
        voto2 = voto2*100
        percentuale = voto2/totale
        print ("il secondo ha vinto con", percentuale, "% dei voti")
    else:
        print ("i voti sono uguali, elezione conclusa in parità")

elif programma == 2:

    lista = []
    candidato1 = input ("nome del candidato 1")
    candidato2 = input ("nome del candidato 2")
    lista.append (candidato1)
    lista.append (candidato2)
    lista.sort
    voti1 = input ("voti del primo")
    voti2 = input ("voti del secondo")
    print (lista)
    if voti1 < voti2:
        print (candidato1,candidato2)
    elif voti2 < voti1:
        print (candidato2, candidato1)

elif programma == 3:
    elenco = []
    media = []
    while True:
        impiegato = input ("nome")
        stipendio = int (input ("stipendio"))
        elenco.append (impiegato)
        media.append (stipendio)
        if impiegato == "-1" or stipendio == -1:
            break 
    somma=0 
    for i in range(len (media)): 
        somma += media[i]
    print (somma/len (media))

else:
    totale = 0
    while True:
        dati_veicolo = input ("scrivi quello che vuoi")
        totale += 1
        if dati_veicolo == "0":
            print (totale)
            break