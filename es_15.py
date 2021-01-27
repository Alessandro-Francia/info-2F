'''
Dato un elenco di nazioni contenuto in una lista e uno delle rispettive capitali in una seconda lista
(nazione e relativa capitale si trovano nella medesima posizione delle rispettive liste), visualizza la capitale di una nazione della quale viene fornito da tastiera il nome,
segnalando con un messaggio di errore il caso in cui la nazione richiesta non sia compresa nell'elenco
'''
nazioni = []
capitali = []

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

def visualizzazione ():
    print ("chiedimi la capitale di un paese:")
    while True:
        paese = input ("")
        if paese == "*":
            break
        elif paese in nazioni:
            print ("la capitale è", capitali [nazioni.index (paese)])
        else:
            print ("nessun dato disponibile per questo paese, inserirne un altro.")

def main ():
    elenco_nazioni ()
    visualizzazione ()

main ()