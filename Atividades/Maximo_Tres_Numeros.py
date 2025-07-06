# Escreva a função maximo que recebe 3 números inteiros como parâmetro e devolve o maior deles.

def maximo (x,y,z):
	if x == y == z:
		return (x)
	elif x > y and x > z:
		return (x)
	elif y > x and y > z:
		return (y)
	else:
		return (z)
		
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

max = maximo (x,y,z)
print (max)