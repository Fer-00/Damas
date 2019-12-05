function jogo{

	jogo.prototype.__init__(){
		tabuleiro = tabuleiro();
		tabuleiro.inicializaTabuleiro();
	}

	jogo.prototype.Jogar(){
		print "Iniciar Jogo?";
		print "1 para Sim; 2 para Não";
		op = raw_input();

		if op == 1{
			print "Indique a posição das peças por linhas e coluna ex{11";		
			aux = Pecas();
			while aux.verificaGanhador() == false{
				tabuleiro.imprime();
				if aux.possivelCapturar(tabuleiro.retornaTabuleiro()){
					print "Existe(m) captura(s) possível(is), vai capturar?";
					cap = raw_input;
					if cap == 1{
						
    	    			(p1,p2) = input("Qual peça quer mover{ ");
        				(p3,p4) = input("}Para onde{ ");
        			}
        		}
        	}
        }else{
        	break
        }
    }
}
