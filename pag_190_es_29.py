'''
Scrivi un programma che legga un reddito da tastiera e calcoli l'importo dell'imposta sul reddito
e la tassazione media. L'osservazione suggerisce di creare opportune strutture dati da utilizzare
nel calcolo dell'imposta.
'''

redditi = [15000, 28000, 55000, 75000, 1000000000000000000]
tasse = [23, 27, 38, 41, 43]
imposta = 0
contatore = 0

while True:

	try:
		reddito = int (input ("inserire il reddito"))
		break
	except:
		print ("non è stato inserito un numero, riprovare")

while True:
	
	if reddito > redditi [contatore]:
		imposta += redditi [contatore] * tasse [contatore]/100
	elif reddito <= redditi [contatore]:
	
		if reddito <= 15000:
			imposta += reddito * tasse [contatore]/100
		else:
			imposta += (reddito - redditi [contatore - 1]) * tasse [contatore]/100
		
		break
	
	contatore += 1

print ("l'imposta sul reddito è", imposta)