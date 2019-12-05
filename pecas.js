function Pecas(){

	var cap = [];
	var isDama = false;
	var pTras = false;
	var qPB = 12; //quantidade de peças brancas
	var qPP = 12; //quantidade de peças negras

	Pecas.prototype.retornaPeca = function(tabuleiro,pos){

		i = pos[0];
		j = pos[1];

		if (tabuleiro[i][j] != ""){
			
			return true;

		}else{

			return false;
		}
	}
		
	Pecas.prototype.moverPeca= function(tabuleiro,posIni, posFim){

		i = posIni[0];
		j = posIni[1];

		k = posFim[0];
		l = posFim[1];

		if (tabuleiro[i][j] == "B"){
			
			if ((k + 1 == i) and ((l - 1 == j) or (l + 1 == j))){

				tabuleiro[k][j] = tabuleiro[i][j];
				tabuleiro[i][j] = " ";
				return tabuleiro;

			}else{

				tabuleiro = tabuleiro;
				return tabuleiro;
			}

		if (tabuleiro[i][j] == "P"){
			
			if ((k - 1 == i) and ((l - 1 == j) or (l + 1 == j))){

				tabuleiro[k][j] = tabuleiro[i][j];
				tabuleiro[i][j] = " ";
				return tabuleiro;

			}else{

				tabuleiro = tabuleiro;
				return tabuleiro;
			}
		}
	
	Pecas.prototype.verificaDama = function (tabuleiro,pos){
		if(tabuleiro[pos[0]][pos[1]] == "B") {
			if (pos[0] == 7){
				isDama = true;
			}else{
				isDama = false;
			}
		if (tabuleiro[pos[0]][pos[1]] == "P") {
			if (pos[0] == 0){
				isDama = true;
			}else{
				isDama = false;
			}

	Pecas.prototype.captura = function (tabuleiro, posIni, posFim){
		if (retornaPeca(tabuleiro, posIni) == true and retornaPeca(tabuleiro, posFim) == false){
			for x in range(0,len(var.cap),2){
				if ((posIni == cap[x]) and (posFim == cap[x+1])){
					posIni = str(posIni);
					posFim = str(posFim);
					tabuleiro[posFim[0]][posFim[1]] = tabuleiro[posIni[0]][posIni[1]]; 
					tabuleiro[posIni[0]][posIni[1]] = "";
					removePeca(tabuleiro,int(posIni[0]),(posIni[1]));
					return tabuleiro;
				}else{
					continue;
				}
			}
			return tabuleiro;
		}else{
			print("Erro");
		}

	Pecas.prototype.verificaGanhador= function (){
		
		if (this.qPB == 0 or this.qPP == 0){
			
			if (var.qPB == 0){
				print ("Pababéns negras ganharam");

			}else{
				print ("Pababéns brancas ganharam");
			}

			resetaTabuleiro();

			return true;

		}else{

			return false;
		}

	Pecas.prototype.removePeca = function (tabuleiro, i, j){
		aux = tabuleiro[i][j];
		tabuleiro[i][j] = "";

		if (aux == "B") {
			qPB --;
			verificaGanhador();
		}else if (aux == "P"){
			qPP --;
			verificaGanhador();
		}else{
			print("Erro");
		}
	}
}