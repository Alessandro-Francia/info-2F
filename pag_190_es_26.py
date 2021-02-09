'''
Con riferimento al dizionario del problema precedente, elenca i numeri di matricola degli
studenti che hanno ottenuto una votazione superiore alla media di tutte le votazioni.
'''

elenco_studenti = {}
elenco_voti = []
print ("inserire i numeri di matricola degli studenti con il relativo voto, non inserire niente per fermare il ciclo")

while True:
	studente = input ("studente:")
	try:
		voto = int(input ("voto:"))
	except ValueError:
		break

	if studente == "":
		break
	else:
		elenco_studenti [studente] = voto
		elenco_voti.append (voto)

try:
	media = sum (elenco_voti)/len (elenco_voti)
	print ("la media dei voti è:", media)
except ZeroDivisionError:
	print ("sono stati inseriti 0 voti, impossibile calcolare la media")
