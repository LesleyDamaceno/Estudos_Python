# Imprime fatorial - Repetições Encaixadas

print ("Digite um número para calcular o fatorial. Digite 0 para finalizar. ")

n = 1
while n != 0:
	n = int(input("Número: "))
	i = fat = 1
	while i <= n:
		fat = fat * i
		i = i + 1
	print (fat)