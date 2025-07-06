# Cálculo do Coeficiente Binomial

def fatorial(n):				# Definição da função que calcula o fatorial
	if (n < 0):
		return (0)
	if (n == 1) or (n == 0):
		return (1)
	else:
		i = fat = 1
		while i <= n:
			fat = fat * i
			i = i + 1
		return(fat)
		
print("Digite primeiro o valor de n e depois o valor de k. Lembre-se que n >= k")		
n = int(input("Digite o valor do parâmetro n: "))
k = int(input("Digite o valor do parâmetro k: "))	

while n < k:
	print("Digite primeiro o valor de n e depois o valor de k. Lembre-se que n >= k")
	n = int(input("Digite o valor do parâmetro n: "))
	k = int(input("Digite o valor do parâmetro k: "))
	
binomial = fatorial(n)/(fatorial(k)*(fatorial(n - k)))
print("O valor do cálculo do Coeficiente Binomial é: ",binomial)