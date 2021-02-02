'''
Scrivi un programma a cui viene passata una parola e riconosce se si tratta di un
palindromo (parole che si leggono uguali anche al contrario) oppure meno.
'''

parola = input ("dimmi la parola")
if parola == parola [::-1]:
    print ("palindroma")
else:
    print ("non palindroma")