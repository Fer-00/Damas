class Pecas:

	self.cap = []
	self.isDama = false
	self.pTras = false
	self.qPB = 12 #quantidade de peças brancas
	self.qPP = 12 #quantidade de peças negras

	def __init__(self):


	def retornaPeca(self,tabuleiro,pos):
		
		pos = str(pos)
		i = pos[0]
		j = pos[1]

		if (tabuleiro[i][j] != ""):
			
			return true

		else:

			return false
		
	def moverPeca(self,tabuleiro,posIni, posFim):

		posIni = str(posIni)
		i = posIni[0]
		j = posIni[1]

		posFim = str(posFim)
		k = posFim[0]
		l = posFim[1]


		if ((k - 1 == i) and ((l - 1 == j) or (l + 1 == j))):

			tabuleiro[k][j] = tabuleiro[i][j]
			tabuleiro[i][j] = " "
			return tabuleiro

		else:

			tabuleiro = tabuleiro
			return tabuleiro
	
	def verificaDama():
		pass

	def captura(self, tabuleiro, posIni, posFim):
		possivelCapturar()
		if (retornaPeca(tabuleiro, posIni) == true and retornaPeca(tabuleiro, posFim) == false):
			for x in range(0,len(self.cap),2):
				if ((posIni == self.cap[x]) and (posFim == self.cap[x+1])):
					posIni = str(posIni)
					posFim = str(posFim)
					tabuleiro[posFim[0]][posFim[1]] = tabuleiro[posIni[0]][posIni[1]] 
					tabuleiro[posIni[0]][posIni[1]] = ""
					removePeca(tabuleiro,int(posIni[0]),(posIni[1]))
					return tabuleiro
				else:
					continue
			return tabuleiro
		else:
			print("Erro")


	def possivelCapturar(self, tabuleiro):

		self.cap.clear()

		for i in range (8):
			
			for j in range(8):
		
				if (j >= 1 and j <= 7):
					if ((tabuleiro[i][j] == "B" and tabuleiro[i+1][j+1] == "P" and tabuleiro[i+2][j+2] == "") or (tabuleiro[i][j] == "B" and tabuleiro[i+1][j-1] == "P" and tabuleiro[i+2][j-2] == "") or (tabuleiro[i][j] == "P" and tabuleiro[i+1][j+1] == "B" and tabuleiro[i+2][j+2] == "") or (tabuleiro[i][j] == "P" and tabuleiro[i+1][j-1]) == "B" and tabuleiro[i+2][j-2] == ""):
						self.cap.append(i,j) 
					else:
						continue

				elif (i == 0):
					if ((tabuleiro[i][j] == "B" and tabuleiro[i+1][j+1] == "P" and tabuleiro[i+2][j+2] == "") or (tabuleiro[i][j] == "P" and tabuleiro[i+1][j+1] == "B" and tabuleiro[i+2][j+2] == "")):
						self.cap.append(i,j) 
					else:
						continue

				elif (i == 7):
					if ((tabuleiro[i][j] == "B" and tabuleiro[i+1][j-1] == "P" and tabuleiro[i+2][j-2] == "") or (tabuleiro[i][j] == "P" and tabuleiro[i+1][j-1] == "B" and tabuleiro[i+2][j-2] == "")):
						self.cap.append(i,j) 
					else
						continue

				else:
					return false

			if (len(self.cap) > 0):
				return true

			else:
				return false

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

	def removePeca(tabuleiro, i, j):
		aux = tabuleiro[i][j]
		tabuleiro[i][j] = ""

		if (aux == "B") :
			qPB --
			verificaGanhador()
		elif (aux == "P"):
			qPP --
			verificaGanhador()
		else:
			print("Erro")	