'''
Aggiungi alla classe Atleta un metodo chiamato effettua_visita che ponga
l'attributo visita_medica uguale a True
'''

class Atleta ():
	visita_medica = False
	squadra = ""
	def contratto (self, nome_squadra):
		self.squadra = nome_squadra
	def effettua_visita (self):
		visita_medica = True