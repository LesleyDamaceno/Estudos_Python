# Escreva um programa que recebe como entradas (utilize a função input) dois números 
# inteiros correspondentes à largura e à altura de um retângulo, respectivamente. 
# O programa deve imprimir, usando repetições encaixadas (laços aninhados), 
# uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

largura = int(input("Digite o valor da largura do retângulo: "))
altura = int(input("Digite o valor da altura do retângulo: "))

while largura <= 0 or altura <= 0:
	largura = int(input("Digite o valor da largura do retângulo: "))
	altura = int(input("Digite o valor da altura do retângulo: "))

aux = 1
while aux <= altura:
	i = 0
	while i < largura:
		print ("#", end = "")
		i = i + 1
	print ()
	aux = aux + 1
		