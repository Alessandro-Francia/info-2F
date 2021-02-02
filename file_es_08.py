lista = []
lista2 = []
a = int (input ("inserire a"))
b = int (input ("inserire b"))

if a > b:
    for n in range (b,a+1):
        lista.append (n)
elif a < b:
    for n in range (a,b+1):
        lista.append (n)
else:
    lista.append (a)

lista.sort ()
print ("la sequenza è", lista)

for elemento in lista:
    elemento *= 2
    lista2.append (elemento)

print ("la sequenza moltplicata per 2 è", lista2)