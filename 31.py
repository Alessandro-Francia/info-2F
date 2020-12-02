binario = []
numero = int (input ("dimmi un numero naturale"))
while True:

    quoziente = int (numero/2)
    resto = numero % 2
    if resto == 1:
        binario.append (1)
    else:
        binario.append (0)
    numero = quoziente
    
    if quoziente == 0:
        break

binario.reverse ()
print (binario)