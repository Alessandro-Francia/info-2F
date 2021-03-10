'''
Elenca proprietà e metodi della classe Prodotto.
'''

class Prodotto:
	costi_produzione = 0
	def __init__ (self):
		self.costi_produzione = 10


prodotto1 = Prodotto()
print (prodotto1.__dict__)