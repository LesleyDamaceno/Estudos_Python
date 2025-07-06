# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro 
# e devolve o maior número primo menor ou igual ao número passado à função.


def primo(n):				# Verifica se um número é primo
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
		

def maior_primo (x):			# Verifica o maior primo
	i = x
	resultado = primo(i)
	while i <= x or resultado == False:
		resultado = primo(i)
		if resultado == True:
			return (i)	
		else:
			i = i - 1
		
n = int(input("Digite um número inteiro maior ou igual a 2: "))

while n < 2:
	n = int(input("Digite um número inteiro maior ou igual a 2: "))
if n == 2:
	print (n)
else:
	resposta = maior_primo(n)
	print(resposta)