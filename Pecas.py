class Pecas:

	def __init__(self):
		
		self.isDama = False
		self.pTras = False
		self.qPB = 12 
		self.qPP = 12 

	def retornaPeca(self,tabuleiro,pos):
		
		pos = str(pos)
		i = int(pos[0])
		j = int(pos[1])

		if (tabuleiro[i][j] == "B" or tabuleiro[i][j] == "P"):
			
			return True

		else:

			return False
		
	def moverPeca(self,tabuleiro,posIni, posFim):

		posIni = str(posIni)
		i = int(posIni[0])
		j = int(posIni[1])

		posFim = str(posFim)
		k = int(posFim[0])
		l = int(posFim[1])
		
		if (tabuleiro[i][j] == "B"):
			
			if ((k + 1 == i) and ((l - 1 == j) or (l + 1 == j))):

				tabuleiro[k][l] = tabuleiro[i][j]
				tabuleiro[i][j] = " "
				return tabuleiro

			else:

				tabuleiro = tabuleiro
				return tabuleiro

		if (tabuleiro[i][j] == "P"):
			
			if ((k - 1 == i) and ((l - 1 == j) or (l + 1 == j))):

				tabuleiro[k][l] = tabuleiro[i][j]
				tabuleiro[i][j] = " "
				return tabuleiro

			else:

				return tabuleiro
	
	def verificaDama(self,tabuleiro,pos):
		if(tabuleiro[pos[0]][pos[1]] == "B") :
			if (pos[0] == 7):
				self.isDama = True
				self.pTras = True
			else:
				self.isDama = False
				self.pTras = False
		if (tabuleiro[pos[0]][pos[1]] == "P") :
			if (pos[0] == 0):
				self.isDama = True
				self.pTras = True
			else:
				self.isDama = False
				self.pTras = False

	def captura(self, tabuleiro, posIni, posFim):
		possivelCapturar()
		if (retornaPeca(tabuleiro, posIni) == True and retornaPeca(tabuleiro, posFim) == False):
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
		
				if (j >= 1 and j <= 6):
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
					else:
						continue

				else:
					return False

			if (len(self.cap) > 0):
				return True

			else:
				return False

	def verificaGanhador(self):
		
		if (self.qPB == 0 or self.qPP == 0):
			
			if (self.qPB == 0):
				print ("Pababens negras ganharam")

			else:
				print ("Pababens brancas ganharam")

			resetaTabuleiro()

			return True

		else:

			return False

	def removePeca(tabuleiro, i, j):
		aux = tabuleiro[i][j]
		tabuleiro[i][j] = ""

		if (aux == "B") :
			qPB = qPB - 1
			verificaGanhador()
		elif (aux == "P"):
			qPP = qPP - 1
			verificaGanhador()
		else:
			print("Erro")	