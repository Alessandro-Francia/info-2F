'''
Elenca proprietà e metodi della classe Prodotto.
'''

class Prodotto:
	costi_produzione = 0
	def __init__ (self, costi):
		self.costi_produzione = costi

	def elenca(self):
		print ("il prodotto è costato", self.costi_produzione, "€")

prodotto1 = Prodotto(10)
prodotto1.elenca ()