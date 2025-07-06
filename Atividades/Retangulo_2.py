# Escreva um programa que recebe como entradas (utilize a função input) dois números 
# inteiros correspondentes à largura e à altura de um retângulo, respectivamente. 
# O programa deve imprimir, usando repetições encaixadas (laços aninhados), 
# uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.
# Agora imprima os retângulos sem preenchimento, de forma que os caracteres que não 
# estiverem na borda do retângulo sejam espaços.

largura = int(input("Digite o valor da largura do retângulo: "))
altura = int(input("Digite o valor da altura do retângulo: "))

while largura <= 0 or altura <= 0:
	largura = int(input("Digite o valor da largura do retângulo: "))
	altura = int(input("Digite o valor da altura do retângulo: "))
	
aux = 1
while aux <= altura:
	i = 1
	if aux == 1 or aux == altura:
		while i < largura:
			print ("#", end = "")
			i = i + 1
		print ("#")
	else:
		while i < largura:
			if i == 1:
				print ("#", end = "")
			else:
				print (" ", end = "")
			i = i + 1
		print ("#")
	aux = aux + 1