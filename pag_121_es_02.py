'''
Data la parabola y = ax^2 + bx + c, definisci tre funzioni per calcolarne i punti significativi: vertice, fuoco,
intersezione con gli assi. Le tre funzioni ricevono come parametri i coefficienti a, b, c e restituiscono il valore calcolato.
'''
'''
import numpy as np

def calcolo_intersezioni (a,b,c):
    matrice_coefficenti = np.array ([[a,b,1],[0,1,0],[0,0,0]])
    matrice_noti = np.array ([1,-1])
    intersezione_y = np.linalg.solve (matrice_coefficenti, matrice_noti)
    return intersezione_y

print (calcolo_intersezioni (1,0,0))
'''

def calcolo_vertice (a,b,c):
    x = -b/(2*a)
    y = -(b**2-4*a*c)/(4*a)
    print ("le coordinate del vertice sono", x,",", y)
    return x,y

def calcolo_fuoco (a,b,c):
    x = -b/(2*a)
    y = (1-(b**2-4*a*c))/(4*a)
    print ("le coordinate del fuoco sono", x,",", y)
    return x,y

print ("vuoi calcolare il vertice o il fuoco?")
scelta = input ()

if scelta == "vertice":
    calcolo_vertice (int (input ("inserire a")), int (input ("inserire b")), int (input ("inserire c")))
else:
    calcolo_fuoco (int (input ("inserire a")), int (input ("inserire b")), int (input ("inserire c")))