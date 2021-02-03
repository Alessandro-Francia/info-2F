nazioni = []
capitali = []
nazioni_diz = {}



def elenco ():
    print ("inserire le nazioni e le relative capitali, inserire invece * per fermare il ciclo.")
    while True:
        nazione = input ("nazione:")
        capitale = input ("capitale:")
        if nazione == "*" or capitale == "*":
            break
        else:
            nazioni.append (nazione)
            capitali.append (capitale)
            nazioni_diz [capitale] = nazione

def visualizzazione ():
    print ("chiedimi la capitale di un paese:")

    while True:
        città = input ("")
        if città == "*":
            break
        elif città in capitali:
            print ("il paese di cui", città, "è la capitale è", nazioni_diz [città])
            print ("premere * se non si vuole più inserire niente, altrimenti inserire un altra capitale")
        else:
            print ("nessun dato disponibile per questa capitale, inserirne un altro")

def main ():
    elenco ()
    visualizzazione ()

main ()