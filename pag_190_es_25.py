'''
I voti assegnati a 30 studenti di una classe in una prova di italiano sono memorizzati
in un dizionario che ha per chiave la matricola, mentre il valore associato è il voto.
Elenca i risultati in ordine crescente di voto e successivamente visualizza quali voti
diversi tra loro sono stati assegnati, riducendo a uno i voti uguali.
'''

elenco_studenti = {}
elenco_voti = []
print ("inserire i numeri di matricola degli studenti con il relativo voto, non inserire niente per fermare il ciclo")

while True:
	studente = input ("studente:")
	if studente == "":
		break
	try:
		voto = int(input ("voto:"))
	except ValueError:
		break
	
	elenco_studenti [studente] = voto
	elenco_voti.append (voto)

elenco_voti.sort ()
print ("sono stati assegnati questi voti:", elenco_voti)

print ("i voti diversi assegnati sono stati:", set (elenco_voti))