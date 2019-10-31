class Pecas:

	self.isDama = false
	self.pTras = false
	self.qPB = 12 #quantidade de peças brancas
	self.qPP = 12 #quantidade de peças negras

	def __init__(self):


	def retornaPeca():
		pass
		
	def moverPeca():
		pass

	def isDama():
		pass

	def captura():
		pass

	def verificaGanhador(self):
		
		if (self.qPB == 0 or self.qPP == 0):
			
			ganhador = true

			if (self.qPB == 0):
				print ("Pababéns negras ganharam")

			else:
				print ("Pababéns brancas ganharam")

			resetaTabuleiro()

		else:

			ganhador = false