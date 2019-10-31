from Pecas import Pecas

class Tabuleiro():
	
	tabuleiro = []	

	def __init__(self):

		for i in range(8):
			aux = []
			for j in range(8):
				aux.append("t")

			self.tabuleiro.append(aux)

	def inicializaTabuleiro (self):
		for i in range(8):
			for j in range(8):
				if (i == 0) or (i == 2):
					if (j == 0) or (j == 2) or (j == 4) or (j == 6):
						self.tabuleiro[i][j] = ("B")
					else:
						self.tabuleiro[i][j] = (" ")
				elif (i == 1):
					if (j == 1) or (j == 3) or (j == 5) or (j == 7):
						self.tabuleiro[i][j] = ("B")
					else:
						self.tabuleiro[i][j] = (" ")

				elif (i == 5) or (i == 7):
					if (j == 1) or (j == 3) or (j == 5) or (j == 7):
						self.tabuleiro[i][j] = ("P")
					else:
						self.tabuleiro[i][j] = (" ")

				elif (i == 6):
					if (j == 0) or (j == 2) or (j == 4) or (j == 6):
						self.tabuleiro[i][j] = ("P")
					else:
						self.tabuleiro[i][j] = (" ")
				else:
					self.tabuleiro[i][j] = (" ")

	def imprime(self):
		
		for x in range(8):
			print ("%3i"%x, end=' ')

		for i in range(8):
			print('')
			print("-"*33)
			#print ("%i"%i),
			for j in range(8):
				print ("|",self.tabuleiro[i][j],end='')
				print (" ", end='');

	def mover(self, posIni,posFim):
		
		ini = Pecas()
		fim = Pecas()

		if (ini.retornaPeca(self.tabuleiro, posIni) == true and fim.retornaPeca(self.tabuleiro, posFim) == false):

			if (fim.moverPeca(posIni, posFim) != false):

				imprime()

			else:

				print ("Movimento Irregular")

		else:

			print ("Movimento Irregular")