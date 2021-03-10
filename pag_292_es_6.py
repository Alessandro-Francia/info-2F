'''
Definisci il metodo assegna_prezzo della classe Prodotto.
'''

class Prodotto:
	costi_produzione = 0
	prezzo = 0
	def __init__ (self, costi):
		self.costi_produzione = costi

	def assegna_prezzo (self, prezzo):
		self.prezzo = prezzo

	def elenca(self):
		print ("il prodotto è costato", self.costi_produzione, "€, il suo prezzo è", self.prezzo, "€")

prodotto1 = Prodotto (10)
prodotto1.assegna_prezzo (15)
prodotto1.elenca ()