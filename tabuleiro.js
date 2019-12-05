function tabuleiro(){

from Pecas import Pecas
	
	tabuleiro = []	

	function.prototype.__init__= function (){

		for i in range(8){
			aux = [];
			for j in range(8){
				aux.append("");
			}
			this.tabuleiro.append(aux)
		}
	}

	function.prototype.inicializaTabuleiro = function (){
		for i in range(8){
			for j in range(8){
				if (i == 0) or (i == 2){
					if (j == 0) or (j == 2) or (j == 4) or (j == 6){
						this.tabuleiro[i][j] = ("B");
					}else{
						this.tabuleiro[i][j] = (" ");
					}
				}else if (i == 1){
					if (j == 1) or (j == 3) or (j == 5) or (j == 7){
						this.tabuleiro[i][j] = ("B");
					}else{
						this.tabuleiro[i][j] = (" ");
					}
				}else if (i == 5) or (i == 7){
					if (j == 1) or (j == 3) or (j == 5) or (j == 7){
						this.tabuleiro[i][j] = ("P");
					}else{
						this.tabuleiro[i][j] = (" ");
					}
				}else if (i == 6){
					if (j == 0) or (j == 2) or (j == 4) or (j == 6){
						this.tabuleiro[i][j] = ("P");
					}else{
						this.tabuleiro[i][j] = (" ");
					}
				}else{
					this.tabuleiro[i][j] = (" ");
				}
			}
		}
	}

	function.prototype.imprime = function (){
		
		for x in range(8){
			print ("%3i"%x, end='');
		}

		for i in range(8){
			print('');
			print("-"*33);
			#print ("%i"%i);
			for j in range(8){
				print ("|",this.tabuleiro[i][j],end='');
				print (" ", end='');
			}
		}
	}

	function.prototype.mover= function (posIni,posFim){
		
		ini = Pecas();
		fim = Pecas();

		if (ini.retornaPeca(this.tabuleiro, posIni) == true and fim.retornaPeca(this.tabuleiro, posFim) == false){

			if (fim.moverPeca(this.tabuleiro,posIni, posFim)){

				if (this.tabuleiro = fim.moverPeca(posIni, posFim) != this.tabuleiro){
				
					imprime();

				}else{

					print ("Movimento Irregular");

			}else{

				print ("Movimento Irregular");

		}else{

			print ("Movimento Irregular");
		}

	function.prototype.Capturar= function (){
		aux = Pecas();

		if (aux.captura(this.tabuleiro,posIni,posFim) == true) {
			if (this.tabuleiro = aux.captura(this.tabuleiro,posIni,posFim) != this.tabuleiro){
				
					imprime();

				}else{

					print ("Movimento Irregular");
				}
		}else{
			print("Movimento Irregular");
		}
	}
	function.prototype.retornaTabuleiro= function (){
		return this.tabuleiro;


		inicializaTabuleiro();		
		imprime();
	}
}