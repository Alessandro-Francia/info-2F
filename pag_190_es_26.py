'''
Con riferimento al dizionario del problema precedente, elenca i numeri di matricola degli
studenti che hanno ottenuto una votazione superiore alla media di tutte le votazioni.
'''

elenco_studenti = {}
elenco_voti = []
elenco_medie = []
print ("inserire i numeri di matricola degli studenti con il relativo voto, non inserire niente per fermare il ciclo")

while True:
	studente = input ("studente:")
	if studente == "":
		break
	try:
		voto = int(input ("voto:"))
	except ValueError:
		break
	elenco_studenti [voto] = studente
	elenco_voti.append (voto)

try:
	media = sum (elenco_voti)/len (elenco_voti)
except ZeroDivisionError:
	print ("sono stati inseriti 0 voti, impossibile calcolare la media")

for e in elenco_voti:
	if e > media:
		if elenco_studenti [voto] not in elenco_medie:
			elenco_medie.append (elenco_studenti [voto])

print ("gli studenti con un voto superiore alla media sono", elenco_medie)