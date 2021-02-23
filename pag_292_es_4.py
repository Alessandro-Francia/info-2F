'''
Aggiungi alla classe Atleta un metodo per visualizzare i dati del giocatore
'''
class Atleta ():
	visita_medica = False
	squadra = ""
	
	def contratto (self, nome_squadra):
		self.squadra = nome_squadra
	def effettua_visita (self):
		self.visita_medica = True
	def visualizza (self):
		print ("l'atleta gioca nei", self.squadra)
		if self.visita_medica == True:
			print ("l'atleta ha svolto la visita")
		else:
			print ("l'atleta non ha svolto la visita")