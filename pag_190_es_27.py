'''
Organizza con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici.
Fornito poi il nome della persona, il programma visualizza il suo numero di telefono
oppure un messaggio nel caso la persona non sia presente nella rubrica.
'''

elenco_numeri = {}

print ("inserire i nomi dei contatti con il relativo numero di telefono, non inserire niente per fermare il ciclo")

while True:
	nome = input ("nome:")
	try:
		numero = int (input ("numero:"))
	except ValueError:
		break

	if nome == "":
		break
	else:
		elenco_numeri [nome] = numero

print ("inserire contatto di cui si vuole il numero, non inserire niente per fermare il programma")

while True:
	richiesta = input ("")
	if richiesta == "":
		break
	elif richiesta in elenco_numeri:
		print ("il numero di telefono è:", elenco_numeri [richiesta])
		print ("inserire un altro numero")
	else:
		print ("la persona non è presente nella rubrica, inserire un altro nome")