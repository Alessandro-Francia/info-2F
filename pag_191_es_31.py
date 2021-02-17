'''
Un'azienda vende prodotti in tutta Iralia e la rete di vendita è suddivisa in quattro zone:
Nord, Centro, Sud e Isole. Dopo aver acquisito in un array il fatturato nelle quattro zone,
calcola il totale del fatturato e i valori in percentuale delle vendite nelle quattro zone.
'''

nord = int (input ("inserire il fatturato del nord"))
sud = int (input ("inserire il fatturato del sud"))
centro = int (input ("inserire il fatturato del centro"))
isole = int (input ("inserire il fatturato delle isole"))

zone = {
	"nord" : nord,
	"sud" : sud,
	"centro" : centro,
	"isole" : isole
}

totale = nord + sud + centro + isole
print ("il fatturato totale è ", totale)

for key in zone:
	print ("il fatturato in percentuale del", key, "è", zone [key] * 100 / totale, "%")