'''
In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto
"rövarspråket", che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni
consonante di una parola e inserire una "o" nel mezzo. Ad esempio la parola
"mangiare" diventa "momanongogiarore".
Scrivi una programma in grado di tradurre una parola o frase passata tramite input in
"rövarspråket".
Dopo aver tradotto una frase, il programma dovrå chiedere all'utente se intende
tradume un'altra, e in caso di risposta positiva, dovrå attendere Ilinserimento di una
nuova parola da parte delltutente.
'''

vocali = ["a","e","i","o","u", " "]

while True:

    italiano = input ("dimmi una parola o una frase in italiano")
    rovarspraket = ""
    for lettera in italiano:
        if lettera not in vocali:
            rovarspraket += lettera + "o" + lettera
        else:
            rovarspraket += lettera
    print ("la parola in rovarspraket è", rovarspraket)

    continuare = input ("scrivi 'si' se vuoi inserirne un'altra    ")
    if continuare != "si":
        break