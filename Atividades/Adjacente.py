# Exercício - Escreva um programa que receba um número inteiro na entrada e verifique 
# se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. 
# Caso exista, imprima "sim"; se não existir, imprima "não".

n = int(input("Digite um número inteiro: "))

restoum = 0
restodois = 1

while (n // 10 != 0 and restoum != restodois):
	divisaoum = n // 10
	restoum = n % 10
	restodois = divisaoum % 10
	n = n // 10
	if restoum == restodois:
		print("sim")
if restoum != restodois:
	print("não")