# Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve:
# 'Fizz' se o número for divisível por 3 e não for divisível por 5;
# 'Buzz' se o número for divisível por 5 e não for divisível por 3;
# 'FizzBuzz' se o número for divisível por 3 e por 5;
# Caso o número não seja divisível 3 e também não seja divisível por 5, 
# ela deve devolver o número recebido como parâmetro.


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
		
		
def divisivel5 (n):
	if (n % 10 == 5) or (n % 10 == 0):
		resultado = True
		return (resultado)
	else: 
		resultado = False
		return (resultado)

def fizzbuzz (n):
	div3 = divisivel3 (n)
	div5 = divisivel5 (n)
	if div3 == True and div5 == True:
		return ("FizzBuzz")
	elif div3 == True and div5 == False:
		return ("Fizz")
	elif div3 == False and div5 == False:
		return (n)
	else:
		return ("Buzz")
	
	
n = int(input("Digite um número inteiro diferente de 0: "))
while n == 0:
	n = int(input("Digite um número inteiro diferente de 0: "))
resposta = fizzbuzz (n)
print (resposta)