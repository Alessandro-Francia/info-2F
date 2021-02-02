'''
Risolvi il problema precedente partendo da due liste che generano un dizionario con la nazione come chiave e la capitale come valore.
Successivamente interroga il dizionario pre visualizzare la capitale di una nazione.
'''

nazioni = []
capitali = []
capitali_diz = {}



def elenco_nazioni ():
    print ("inserire le nazioni e le relative capitali, inserire invece * per fermare il ciclo.")
    while True:
        nazione = input ("nazione:")
        capitale = input ("capitale:")
        if nazione == "*" or capitale == "*":
            break
        else:
            nazioni.append (nazione)
            capitali.append (capitale)
            capitali_diz [nazione] = capitale

def visualizzazione ():
    print ("chiedimi la capitale di un paese:")

    while True:
        paese = input ("")
        if paese == "*":
            break
        elif paese in nazioni:
            print ("la capitale è", capitali_diz [paese])
            print ("premere * se non si vuole più inserire niente, altrimenti inserire un altro paese")
        else:
            print ("nessun dato disponibile per questo paese, inserirne un altro")

def main ():
    elenco_nazioni ()
    visualizzazione ()

main ()