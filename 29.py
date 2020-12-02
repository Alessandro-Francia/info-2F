print ("digita 0 per terminare l'elenco")
nomi = []
escursioni_termiche = []
contatore = 0

while True:

    città = input ("nome della città:    ")
    max_gradi = int (input ("temperatura massima prefissata:    "))
    min_gradi = int (input ("temperatura minima prefissata:    "))
    escursione_termica = (max_gradi - min_gradi)
    nomi.append (città)
    escursioni_termiche.append (escursione_termica)
    
    if città == "0" or max_gradi == 0 or min_gradi == 0:
        for i in nomi:
            indice = nomi.index (i)
            max_gradi_2 = int (input ("temperatura massima oggi:    "))
            min_gradi_2 = int (input ("temperatura minima oggi:    "))
            escursione_termica_2 = (max_gradi_2 - min_gradi_2)

            if escursione_termica_2 > escursioni_termiche [indice]:
                contatore += 1
        break
print ("le città che hanno avuto un'escursione termica maggiore rispetto alla prefissata sono", contatore)