calcolo = input ("vuoi calcolare l'area di un quadrato, rettangolo, triangolo o cerchio?")


if calcolo == "quadrato":
    l = int (input ("quant'è il lato?"))
    print ("l'area è", l**2)
elif calcolo == "rettangolo" or calcolo == "triangolo":
    b = int (input ("quant'è la base?"))
    h = int (input ("quant'è l'altezza?"))
    if calcolo == "rettangolo":
        print ("l'area è", b*h)
    else:
        print ("l'area è", b*h/2)
else:
    r = int (input ("quant'è il raggio?"))
    print ("l'area è", r**2*3,14159265358)