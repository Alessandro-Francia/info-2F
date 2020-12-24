'''
Crea un programma che scriva la differenza di due numeri a e b se il loro prodotto è maggiore di 10,
oppure la loro somma se il prodotto è minore o uguale a 10.
'''

print ("inserire a")
a = int (input ())
print ("inserire b")
b = int (input ())
if a*b > 10:
    print (a-b)
else:
    print (a+b)