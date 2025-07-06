# Jogo do NIM -  Versão Final

def main ():
	print ("\n Bem-vindo ao jogo do NIM! Você jogará contra o computador. Escolha: \n")
	print (" 0 - Para ler as regras do jogo" )
	print (" 1 - Para jogar uma partida isolada ")
	resposta = int(input(" 2 - Para jogar um campeonato \n"))
	
	while resposta != 0 and resposta != 1 and resposta != 2:
		print ("0 - Para ler as regras do jogo" )
		print ("1 - Para jogar uma partida isolada ")
		resposta = int(input("2 - Para jogar um campeonato \n"))
	
	if resposta == 0:
		print ("\n Você escolheu ler a regras! ")
		regras()
	elif resposta == 1:
		print (" Você escolheu jogar uma partida!\n")
		partida ()
	else:
		print (" Você escolheu campeonato!\n")
		usuario = 0
		computador = 0
		i = 1
		
		while i <= 3:
			print (" ***** Rodada", i,"! *****\n")
			rodada = partida ()
			if rodada == 0:
				usuario = usuário + 1
			else:
				computador = computador + 1 
			i = i + 1
		print (" **** Final do campeonato! ****\n")
		if computador > usuario:
			print (" Computador venceu! \n")
		else:
			print (" Você venceu!!\n")
		print (" Placar: Você", usuario, "X", computador, "Computador")


def regras():
	print ()
	print (" O jogo do Nim é um jogo de estratégia em que os jogadores, alternadamente,") 
	print (" removem as peças do jogo. Ganha aquele que conseguir remover as últimas peças.")
	print ()
	print (" Regras Básicas:")
	print ()
	print (" 1. Setup:")
	print (" O jogo começa com a quantidade de n peças. Você escolherá o valor de n. \n")
	print (" 2. Jogada:")
	print (" Cada jogador pode, na sua vez, remover no máximo um valor m de peças. Você escolherá quantas")
	print (" m peças poderão ser retiradas.\n")
	print (" 3. Vencedor:")
	print (" O jogador que remover as últimas peças vence o jogo. \n")
	
	main()


def computador_escolhe_jogada (n,m):
	retirapeca = 1
	
	while retirapeca != m:
		if (n - retirapeca) % (m+1) == 0:
			return (retirapeca)
		else:
			retirapeca = retirapeca + 1
	return retirapeca


def usuario_escolhe_jogada (n,m):
	retirapeca = int(input(" Quantas peças você vai retirar? "))
	while (retirapeca > m) or (retirapeca < 1):
		print (" Oops! Jogada inválida! Tente de novo. \n")
		retirapeca = int(input(" Quantas peças você vai retirar? "))
	return (retirapeca)
	
	
def partida ():
	n = int(input(" Quantas peças?: "))
	m = int(input(" Limite de peças por jogada: "))
	print ()
		
	while n < 0 and m < 0 and m > n:
		n = int(input(" Quantas peças?: "))
		m = int(input(" Limite de peças por jogada: "))
		print ()
		
	if (n % (m+1)) == 0:
		print (" Você começa!\n")
		cont = 1
	else: 
		print (" Computador começa!\n")
		cont = 2
	
	while (n > 0): 
		if (cont % 2 != 0):
			jogada = int (usuario_escolhe_jogada (n,m))
			n = n - jogada
			if jogada == 1:
				print (" Você tirou uma peça.")
			else:
				print (" Você tirou", jogada, "peças.")
			print (" Agora restam", n, "peças no tabuleiro.\n")
	
		else:
			jogada = int (computador_escolhe_jogada (n,m))
			n = n - jogada
			if jogada == 1:
				print (" O computador tirou uma peça.")
			else:
				print (" O computador tirou", jogada, "peças.")
			print (" Agora restam", n, "peças no tabuleiro.\n")	
		cont = cont + 1
	
	if cont % 2 == 0:
		print (" Você venceu!!\n")
		return (0)
	else: 
		print (" Computador venceu!!\n")
		return (1)
	
main()