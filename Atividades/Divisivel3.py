def divisivel3 (n):
	valor = 0
	while (n // 10 != 0) or (n % 10 != 0):
		resto = n % 10
		valor = valor + resto
		n = n // 10
	if ((valor % 3) == 0):
		resultado = True
		return (resultado)
	else: 
		resultado = False
		return (resultado)
		
n = int(input("Digite um número: "))
resposta = divisivel3(n)
print (resposta)