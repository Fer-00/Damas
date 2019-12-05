from Tabuleiro import Tabuleiro
from Pecas import Pecas

class Jogo:

	def __init__(self):
		tabuleiro = Tabuleiro()
		tabuleiro.inicializaTabuleiro()

	def Jogar(self):
		print "Iniciar Jogo?"
		print "1 para Sim; 2 para Nao"
		op = raw_input()

		if op == "1":
			print "Indique a posicao das pecas por linhas e coluna ex:11"		
			aux = Pecas()
			tabuleiro = Tabuleiro()
			while aux.verificaGanhador() == False:
				tabuleiro.imprime()
				ini = int(input("Qual peca quer mover:"))
				fim = int(input("Para onde: "))

				if ini != "" and fim != "":
			
					tabuleiro = tabuleiro.mover(ini,fim)

