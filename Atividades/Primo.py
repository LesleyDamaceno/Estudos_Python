# Verifica se um número é primo

def primo(n):
	i = 0
	cont = 0
	primo = False
	while i <= n or cont < 2:
		i = i + 1
		x = n % i
		if x == 0:
			cont = cont + 1
	if cont <= 2:
		primo = True
		return (primo)
	else:
		return (primo)
	
n = int(input("Digite um número inteiro maior que 1: "))

while n <= 1:
	n = int(input("Digite um número inteiro maior que 1: "))

resultado = primo(n)
if resultado == True:
	print ("É primo")
else:
	print ("Não é primo")