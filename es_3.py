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