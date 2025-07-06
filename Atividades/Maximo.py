# Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

def maximo (x,y):
	if x == y:
		return (x)
	if x < y:
		return (y)
	else:
		return (x)

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

max = maximo (x,y)
print (max)